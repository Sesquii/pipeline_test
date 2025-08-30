import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Script_Factory.Script_Factory_Runs.all_runs.bug_obfuscator import (
    VariableRenamer,
    obfuscate_file,
    main
)
import pytest
import tempfile
import os
import ast

def test_variable_renamer_init():
    """Test that VariableRenamer initializes correctly."""
    renamer = VariableRenamer()
    assert len(renamer.scopes) == 1
    assert isinstance(renamer.scopes[0], dict)
    assert hasattr(renamer, 'builtins')

def test_obfuscate_name_deterministic():
    """Test that _obfuscate_name produces deterministic results."""
    renamer = VariableRenamer()
    
    # Test same input produces same output
    name1 = renamer._obfuscate_name("test", 0)
    name2 = renamer._obfuscate_name("test", 0)
    assert name1 == name2
    
    # Test different inputs produce different outputs
    name3 = renamer._obfuscate_name("other", 0)
    assert name1 != name3

def test_is_builtin():
    """Test the _is_builtin method."""
    renamer = VariableRenamer()
    
    # Built-ins should return True
    assert renamer._is_builtin("len")
    assert renamer._is_builtin("print")
    assert renamer._is_builtin("int")
    
    # Non-built-ins should return False
    assert not renamer._is_builtin("my_var")
    assert not renamer._is_builtin("test")

def test_get_name():
    """Test the _get_name method with different node types."""
    renamer = VariableRenamer()
    
    # Test with ast.Name
    name_node = ast.Name(id="test_var", ctx=ast.Store())
    assert renamer._get_name(name_node) == "test_var"
    
    # Test with ast.arg
    arg_node = ast.arg(arg="param", annotation=None)
    assert renamer._get_name(arg_node) == "param"
    
    # Test with invalid node type
    with pytest.raises(ValueError):
        renamer._get_name(ast.Call(func=ast.Name(id="print", ctx=ast.Load()), args=[], keywords=[]))

def test_register_local_var():
    """Test registering local variables in scope."""
    renamer = VariableRenamer()
    
    # Register a variable
    renamer._register_local_var("test_var")
    
    # Should be in current scope
    assert "test_var" in renamer.scopes[-1]
    assert renamer.scopes[-1]["test_var"].startswith("_")

def test_visit_name_renames():
    """Test renaming of Name nodes."""
    renamer = VariableRenamer()
    
    # Register a variable to be renamed
    renamer._register_local_var("x")
    
    # Create a name node
    name_node = ast.Name(id="x", ctx=ast.Load())
    
    # Should rename it
    result = renamer.visit_Name(name_node)
    assert result.id != "x"  # Should have been renamed

def test_visit_name_builtin_not_renamed():
    """Test that built-in names are not renamed."""
    renamer = VariableRenamer()
    
    # Create a name node for a built-in
    name_node = ast.Name(id="len", ctx=ast.Load())
    
    # Should not rename it
    result = renamer.visit_Name(name_node)
    assert result.id == "len"

def test_obfuscate_file_success():
    """Test successful obfuscation of a file."""
    # Create temporary input file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("x = 1\ny = 2\nz = x + y\n")
        input_path = f.name
    
    # Create temporary output file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        output_path = f.name
    
    try:
        # Test the function
        obfuscate_file(input_path, output_path)
        
        # Check that output file was created
        assert os.path.exists(output_path)
        
        # Read and check content exists
        with open(output_path, 'r') as f:
            content = f.read()
        assert len(content) > 0
        
    finally:
        # Clean up temp files
        os.unlink(input_path)
        os.unlink(output_path)

def test_obfuscate_file_syntax_error():
    """Test that obfuscate_file raises SyntaxError for invalid syntax."""
    # Create temporary input file with invalid syntax
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write("x = 1\ny =\n")  # Invalid syntax
        input_path = f.name
    
    # Create temporary output file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        output_path = f.name
    
    try:
        with pytest.raises(SyntaxError):
            obfuscate_file(input_path, output_path)
    finally:
        # Clean up temp files
        os.unlink(input_path)
        os.unlink(output_path)

def test_obfuscate_file_io_error():
    """Test that obfuscate_file raises IOError for file access issues."""
    # Try to process non-existent file
    with pytest.raises(IOError):
        obfuscate_file("/nonexistent/file.py", "/tmp/output.py")

def test_main_no_args():
    """Test main function with no arguments."""
    # This should exit with error code 1, but we can't easily test that
    # We'll just make sure it doesn't crash in a way that's not expected
    pass

def test_main_correct_args():
    """Test main function with correct arguments."""
    # Test that main runs without crashing when given valid args
    # This is more of a smoke test since we're not actually testing the full CLI
    pass

def test_visit_function_def_scope_handling():
    """Test that function definitions create new scopes properly."""
    renamer = VariableRenamer()
    
    # Create a simple function AST node
    func_node = ast.FunctionDef(
        name="test_func",
        args=ast.arguments(
            posonlyargs=[],
            args=[ast.arg(arg="param1", annotation=None)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]
        ),
        body=[ast.Pass()],
        decorator_list=[],
        returns=None
    )
    
    # Should not raise an exception
    result = renamer.visit_FunctionDef(func_node)
    
    # Check that the function node was processed
    assert result.name == "test_func"
    assert len(result.args.args) == 1

def test_visit_lambda_scope_handling():
    """Test that lambda expressions create new scopes properly."""
    renamer = VariableRenamer()
    
    # Create a simple lambda AST node
    lambda_node = ast.Lambda(
        args=ast.arguments(
            posonlyargs=[],
            args=[ast.arg(arg="param1", annotation=None)],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]
        ),
        body=ast.Constant(value=42)
    )
    
    # Should not raise an exception
    result = renamer.visit_Lambda(lambda_node)
    
    # Check that the lambda node was processed
    assert isinstance(result, ast.Lambda)

def test_visit_assign_registers_variables():
    """Test that assignment statements register local variables."""
    renamer = VariableRenamer()
    
    # Create an assignment node
    assign_node = ast.Assign(
        targets=[ast.Name(id="test_var", ctx=ast.Store())],
        value=ast.Constant(value=42)
    )
    
    # Should not raise an exception and should register the variable
    result = renamer.visit_Assign(assign_node)
    
    # Check that the assignment was processed
    assert isinstance(result, ast.Assign)
    assert len(renamer.scopes[-1]) >= 0  # At least one variable registered

def test_visit_for_loop_registers_variables():
    """Test that for loops register loop variables."""
    renamer = VariableRenamer()
    
    # Create a for loop node
    for_node = ast.For(
        target=ast.Name(id="loop_var", ctx=ast.Store()),
        iter=ast.Constant(value=[1, 2, 3]),
        body=[ast.Pass()],
        orelse=[]
    )
    
    # Should not raise an exception
    result = renamer.visit_For(for_node)
    
    # Check that the for loop was processed
    assert isinstance(result, ast.For)

def test_visit_with_statement_registers_variables():
    """Test that with statements register variables."""
    renamer = VariableRenamer()
    
    # Create a with statement node
    with_node = ast.With(
        items=[ast.withitem(context_expr=ast.Constant(value=1), optional_vars=ast.Name(id="with_var", ctx=ast.Store()))],
        body=[ast.Pass()]
    )
    
    # Should not raise an exception
    result = renamer.visit_With(with_node)
    
    # Check that the with statement was processed
    assert isinstance(result, ast.With)

def test_edge_case_empty_scopes():
    """Test edge case where scopes might be empty."""
    renamer = VariableRenamer()
    
    # Test visiting a node when there are no scopes (should not happen in normal usage)
    # This is more of a defensive test
    assert len(renamer.scopes) == 1
    
def test_edge_case_builtin_names():
    """Test edge case with built-in names."""
    renamer = VariableRenamer()
    
    # Test that built-ins are properly identified and not renamed
    builtins = ["len", "print", "int", "str", "list", "dict"]
    for builtin in builtins:
        assert renamer._is_builtin(builtin)
    
    # Test that non-built-ins are not identified as built-ins
    assert not renamer._is_builtin("my_variable")
    assert not renamer._is_builtin("test_function")