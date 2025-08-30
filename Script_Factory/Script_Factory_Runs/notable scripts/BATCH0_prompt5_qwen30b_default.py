#!/usr/bin/env python3
"""
Bug Obfuscator - A tool to rename local variables in Python source code
to obscure their purpose while preserving semantics.

Usage:
    python bug_obfuscator.py input.py output.py
"""

import ast
import sys
import hashlib
from typing import Dict, List, Optional, Tuple, Union


class VariableRenamer(ast.NodeTransformer):
    """
    AST transformer that renames local variables to obfuscated names.
    
    This class maintains a mapping of original variable names to obfuscated names
    within each scope. It ensures that:
    - Same variable name in same scope maps to same obfuscated name
    - Variables with same name in different scopes get independent mappings
    - Built-in names and imports are not renamed
    - Function/class definitions and attributes remain unchanged
    """
    
    def __init__(self):
        # Stack of scopes, each scope is a dict mapping original -> obfuscated names
        self.scopes: List[Dict[str, str]] = [{}]
        # Set of built-in names to avoid renaming
        self.builtins = set(dir(__builtins__))
        
    def _obfuscate_name(self, name: str, scope_depth: int) -> str:
        """
        Generate a deterministic obfuscated name based on original name and scope.
        
        This ensures that repeated runs produce identical obfuscation patterns.
        """
        # Create a hash of the name + scope depth to ensure deterministic mapping
        salt = f"{name}_{scope_depth}"
        hash_digest = hashlib.md5(salt.encode()).hexdigest()
        # Take first 6 hex characters and prefix with underscore for valid Python identifier
        return f"_{hash_digest[:6]}"
    
    def _is_builtin(self, name: str) -> bool:
        """Check if a name is a built-in Python name."""
        return name in self.builtins
    
    def _is_imported(self, node: ast.AST) -> bool:
        """
        Check if the node represents an imported name.
        
        This handles cases like:
        - import math
        - from math import sqrt
        - import math as m
        """
        # For simplicity, we assume that any name in a global context that's 
        # part of an Import or ImportFrom node is imported. This is not perfect,
        # but good enough for our purposes.
        return False  # We'll handle this at the assignment level
    
    def _get_name(self, node: Union[ast.Name, ast.arg]) -> str:
        """Extract the name from Name or arg node."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.arg):
            return node.arg
        else:
            raise ValueError(f"Unexpected node type for name extraction: {type(node)}")
    
    def visit_Import(self, node: ast.Import) -> None:
        """Handle import statements - we don't rename imported names."""
        # Skip processing imports entirely since they're handled differently
        return None
    
    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        """Handle from ... import ... statements."""
        # Skip processing imports entirely
        return None
    
    def _is_assignment_target(self, node: ast.AST) -> bool:
        """
        Determine if the node represents a variable assignment target.
        
        This helps identify when we're defining local variables.
        """
        # Check if this is a direct assignment to a name (e.g., x = 1)
        if isinstance(node, ast.Name):
            return True
        elif isinstance(node, ast.Tuple) or isinstance(node, ast.List):
            # Check if any element is a name (e.g., a, b = 1, 2)
            for elt in node.elts:
                if isinstance(elt, ast.Name):
                    return True
        return False
    
    def visit_Assign(self, node: ast.Assign) -> ast.Assign:
        """Handle assignment statements to identify local variables."""
        # Process targets first (left-hand side of assignments)
        new_targets = []
        for target in node.targets:
            if isinstance(target, ast.Name):
                # This is a simple assignment like x = 1
                self._register_local_var(target.id)
            elif isinstance(target, ast.Tuple) or isinstance(target, ast.List):
                # Handle tuple/list unpacking like a, b = 1, 2
                for elt in target.elts:
                    if isinstance(elt, ast.Name):
                        self._register_local_var(elt.id)
            new_targets.append(self.visit(target))
        node.targets = new_targets
        
        # Visit the right-hand side
        node.value = self.visit(node.value)
        return node
    
    def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.AnnAssign:
        """Handle annotated assignments like x: int = 1."""
        if node.target and isinstance(node.target, ast.Name):
            self._register_local_var(node.target.id)
        node.target = self.visit(node.target)
        node.annotation = self.visit(node.annotation)
        node.value = self.visit(node.value)
        return node
    
    def visit_AugAssign(self, node: ast.AugAssign) -> ast.AugAssign:
        """Handle augmented assignments like x += 1."""
        if isinstance(node.target, ast.Name):
            self._register_local_var(node.target.id)
        node.target = self.visit(node.target)
        node.value = self.visit(node.value)
        return node
    
    def visit_For(self, node: ast.For) -> ast.For:
        """Handle for loops - need to process loop variables."""
        # Process the target (loop variable)
        if isinstance(node.target, ast.Name):
            self._register_local_var(node.target.id)
        elif isinstance(node.target, ast.Tuple) or isinstance(node.target, ast.List):
            for elt in node.target.elts:
                if isinstance(elt, ast.Name):
                    self._register_local_var(elt.id)
        
        node.target = self.visit(node.target)
        node.iter = self.visit(node.iter)
        node.body = self.visit(node.body)
        node.orelse = self.visit(node.orelse)
        return node
    
    def visit_With(self, node: ast.With) -> ast.With:
        """Handle with statements."""
        for item in node.items:
            if item.optional_vars and isinstance(item.optional_vars, ast.Name):
                self._register_local_var(item.optional_vars.id)
            elif item.optional_vars and (isinstance(item.optional_vars, ast.Tuple) or 
                                       isinstance(item.optional_vars, ast.List)):
                for elt in item.optional_vars.elts:
                    if isinstance(elt, ast.Name):
                        self._register_local_var(elt.id)
        
        node.items = [self.visit(item) for item in node.items]
        node.body = self.visit(node.body)
        return node
    
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        """
        Handle function definitions.
        
        We need to create a new scope for function parameters and local variables,
        but not rename the function name itself.
        """
        # Add function name to outer scope (not renamed)
        # But we do want to process parameter names in this scope
        
        # Process function arguments
        for arg in node.args.args:
            self._register_local_var(arg.arg)
        
        # Add default argument values to scope
        if node.args.defaults:
            for default in node.args.defaults:
                self.visit(default)
        if node.args.kw_defaults:
            for kw_default in node.args.kw_defaults:
                if kw_default:
                    self.visit(kw_default)
        
        # Process function body
        old_scope = self.scopes[-1]
        self.scopes.append({})
        try:
            node.body = self.visit(node.body)
        finally:
            self.scopes.pop()
        
        return node
    
    def visit_Lambda(self, node: ast.Lambda) -> ast.Lambda:
        """
        Handle lambda expressions.
        
        Lambda functions have their own scope for parameters and local variables.
        """
        # Create a new scope for lambda parameters
        old_scope = self.scopes[-1]
        self.scopes.append({})
        try:
            # Process arguments
            for arg in node.args.args:
                self._register_local_var(arg.arg)
            
            # Visit the lambda body
            node.body = self.visit(node.body)
        finally:
            self.scopes.pop()
        
        return node
    
    def visit_ListComp(self, node: ast.ListComp) -> ast.ListComp:
        """Handle list comprehensions."""
        # Process comprehensions with their own scopes
        old_scope = self.scopes[-1]
        self.scopes.append({})
        try:
            node.generators = [self.visit(gen) for gen in node.generators]
            node.elt = self.visit(node.elt)
        finally:
            self.scopes.pop()
        
        return node
    
    def visit_SetComp(self, node: ast.SetComp) -> ast.SetComp:
        """Handle set comprehensions."""
        old_scope = self.scopes[-1]
        self.scopes.append({})
        try:
            node.generators = [self.visit(gen) for gen in node.generators]
            node.elt = self.visit(node.elt)
        finally:
            self.scopes.pop()
        
        return node
    
    def visit_DictComp(self, node: ast.DictComp) -> ast.DictComp:
        """Handle dictionary comprehensions."""
        old_scope = self.scopes[-1]
        self.scopes.append({})
        try:
            node.generators = [self.visit(gen) for gen in node.generators]
            node.key = self.visit(node.key)
            node.value = self.visit(node.value)
        finally:
            self.scopes.pop()
        
        return node
    
    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> ast.GeneratorExp:
        """Handle generator expressions."""
        old_scope = self.scopes[-1]
        self.scopes.append({})
        try:
            node.generators = [self.visit(gen) for gen in node.generators]
            node.elt = self.visit(node.elt)
        finally:
            self.scopes.pop()
        
        return node
    
    def visit_Comprehension(self, node: ast.Comprehension) -> ast.Comprehension:
        """Handle comprehensions (used in list/set/dict comprehensions)."""
        # Handle the target variable of the comprehension
        if isinstance(node.target, ast.Name):
            self._register_local_var(node.target.id)
        elif isinstance(node.target, ast.Tuple) or isinstance(node.target, ast.List):
            for elt in node.target.elts:
                if isinstance(elt, ast.Name):
                    self._register_local_var(elt.id)
        
        node.target = self.visit(node.target)
        node.iter = self.visit(node.iter)
        node.ifs = [self.visit(if_) for if_ in node.ifs]
        return node
    
    def visit_Name(self, node: ast.Name) -> ast.Name:
        """Rename Name nodes (variable references)."""
        # Do not rename built-ins or imports
        if self._is_builtin(node.id):
            return node
        
        # Find the appropriate scope and rename if needed
        for scope in reversed(self.scopes):
            if node.id in scope:
                node.id = scope[node.id]
                break
            elif node.id in self.builtins:
                # This is a built-in, do not rename
                break
        
        return node
    
    def visit_arg(self, node: ast.arg) -> ast.arg:
        """Handle function arguments."""
        # Function arguments are local to the function scope
        if node.arg not in self.scopes[-1]:
            obfuscated = self._obfuscate_name(node.arg, len(self.scopes) - 1)
            self.scopes[-1][node.arg] = obfuscated
            node.arg = obfuscated
        
        return node
    
    def _register_local_var(self, name: str):
        """Register a local variable in the current scope."""
        # Do not register built-ins or already registered names
        if name in self.builtins:
            return
        
        # Check if this name is already mapped in current scope
        if name not in self.scopes[-1]:
            obfuscated = self._obfuscate_name(name, len(self.scopes) - 1)
            self.scopes[-1][name] = obfuscated


def obfuscate_file(input_path: str, output_path: str):
    """
    Obfuscate a Python source file by renaming local variables.
    
    Args:
        input_path (str): Path to the input .py file
        output_path (str): Path to the output obfuscated .py file
    
    Raises:
        SyntaxError: If the input file contains invalid Python syntax
        IOError: If there are issues reading or writing files
    """
    try:
        # Read and parse the source code
        with open(input_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        tree = ast.parse(source_code)
        
        # Apply renaming transformation
        renamer = VariableRenamer()
        new_tree = renamer.visit(tree)
        
        # Generate the obfuscated code
        obfuscated_code = ast.unparse(new_tree) if hasattr(ast, 'unparse') else ast.dump(new_tree)
        
        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
            
    except SyntaxError as e:
        raise SyntaxError(f"Invalid syntax in {input_path}: {e}")
    except IOError as e:
        raise IOError(f"Error processing files: {e}")


def main():
    """Main entry point for the script."""
    if len(sys.argv) != 3:
        print("Usage: python bug_obfuscator.py <input_file> <output_file>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        obfuscate_file(input_path, output_path)
        print(f"Successfully obfuscated {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
