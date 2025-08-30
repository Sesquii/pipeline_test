#!/usr/bin/env python3
"""
Bug Obfuscator - A tool to obfuscate Python source code by renaming local variables.

This script reads a Python source file and writes an obfuscated version to another file.
It preserves all semantics but renames local variables to confusing names like _a1b2c3,
while avoiding renaming built-ins, imports, or non-local identifiers.

Usage:
    python bug_obfuscator.py input.py output.py
"""

import ast
import sys
import hashlib
from typing import Dict, List, Set, Tuple, Optional


class VariableRenamer(ast.NodeTransformer):
    """
    A NodeTransformer that renames local variables in a Python AST.
    
    This class tracks variable names by scope and ensures deterministic renaming
    while preserving semantics. It avoids renaming built-ins, imports, and non-local identifiers.
    """

    def __init__(self):
        # Stack of scopes, each scope is a dict mapping original names to obfuscated names
        self.scopes: List[Dict[str, str]] = [{}]
        # Set of built-in names that should not be renamed
        self.builtins: Set[str] = set(dir(__builtins__))
        # Set of imported names that should not be renamed
        self.imported_names: Set[str] = set()
        # Counter for generating new names
        self.name_counter = 0

    def _generate_obfuscated_name(self, original_name: str, scope_depth: int) -> str:
        """
        Generate a deterministic obfuscated name based on the original name and scope depth.
        
        Args:
            original_name: The original variable name.
            scope_depth: The depth of the current scope.
            
        Returns:
            A deterministic obfuscated name.
        """
        # Create a hash of the original name + scope depth for deterministic mapping
        salt = f"{original_name}_{scope_depth}"
        hash_object = hashlib.md5(salt.encode())
        hex_dig = hash_object.hexdigest()[:6]  # Use first 6 hex chars
        
        # Prefix with underscore and append digits to make it look like a variable name
        return f"_{hex_dig}"

    def _is_local_name(self, name: str) -> bool:
        """
        Determine if a name is local and should be obfuscated.
        
        Args:
            name: The name to check.
            
        Returns:
            True if the name should be obfuscated (i.e., it's not builtin or imported).
        """
        return name not in self.builtins and name not in self.imported_names

    def _get_current_scope(self) -> Dict[str, str]:
        """Get the current scope dictionary."""
        return self.scopes[-1]

    def _enter_scope(self):
        """Enter a new scope."""
        self.scopes.append({})

    def _exit_scope(self):
        """Exit the current scope."""
        self.scopes.pop()

    def visit_Module(self, node: ast.Module) -> ast.Module:
        """
        Visit a module node to collect imported names.
        
        This is done before processing the rest of the code to know what's imported.
        """
        # Collect all imported names
        for stmt in node.body:
            if isinstance(stmt, ast.Import):
                for alias in stmt.names:
                    self.imported_names.add(alias.name.split('.')[0])  # Handle 'import a.b'
            elif isinstance(stmt, ast.ImportFrom):
                if stmt.module:
                    for alias in stmt.names:
                        # For 'from x import y' or 'from x import y as z', we collect 'y' or 'z'
                        self.imported_names.add(alias.name)
        
        # Process the module body
        return self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        """
        Visit a function definition.
        
        Enters a new scope for the function's local variables and processes its body.
        """
        # Enter function scope
        self._enter_scope()
        
        # Process function arguments (they are local to the function)
        for arg in node.args.args:
            if isinstance(arg, ast.arg):
                # Add argument names to current scope
                self._rename_in_scope(arg.arg)
                
        # Handle default arguments - these are evaluated in outer scope
        for default in node.args.defaults:
            self.visit(default)
            
        # Process function body
        node.body = [self.visit(stmt) for stmt in node.body]
        
        # Exit function scope
        self._exit_scope()
        
        return node

    def visit_Lambda(self, node: ast.Lambda) -> ast.Lambda:
        """
        Visit a lambda expression.
        
        Enters a new scope for lambda variables and processes its body.
        """
        # Enter lambda scope
        self._enter_scope()
        
        # Process lambda arguments (they are local to the lambda)
        for arg in node.args.args:
            if isinstance(arg, ast.arg):
                self._rename_in_scope(arg.arg)
                
        # Process lambda body
        node.body = self.visit(node.body)
        
        # Exit lambda scope
        self._exit_scope()
        
        return node

    def visit_Comprehension(self, node: ast.Comprehension) -> ast.Comprehension:
        """
        Visit a comprehension.
        
        Comprehensions have their own scope for the target variable.
        """
        # Enter comprehension scope
        self._enter_scope()
        
        # Rename the target variable (e.g., in "for x in y" or "for i, j in enumerate(...)")
        if isinstance(node.target, ast.Name):
            self._rename_in_scope(node.target.id)
        elif isinstance(node.target, ast.Tuple):
            for elt in node.target.elts:
                if isinstance(elt, ast.Name):
                    self._rename_in_scope(elt.id)
        
        # Process other parts of comprehension
        node.iter = self.visit(node.iter)
        node.ifs = [self.visit(if_) for if_ in node.ifs]
        
        # Exit comprehension scope
        self._exit_scope()
        
        return node

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> ast.GeneratorExp:
        """
        Visit a generator expression.
        
        Generator expressions can contain comprehensions and have their own scope.
        """
        # Enter generator expression scope
        self._enter_scope()
        
        # Process generator expressions (they may contain comprehensions)
        node.elt = self.visit(node.elt)
        node.generators = [self.visit(gen) for gen in node.generators]
        
        # Exit generator expression scope
        self._exit_scope()
        
        return node

    def visit_ListComp(self, node: ast.ListComp) -> ast.ListComp:
        """
        Visit a list comprehension.
        
        List comprehensions can contain comprehensions and have their own scope.
        """
        # Enter list comprehension scope
        self._enter_scope()
        
        # Process list comprehension
        node.elt = self.visit(node.elt)
        node.generators = [self.visit(gen) for gen in node.generators]
        
        # Exit list comprehension scope
        self._exit_scope()
        
        return node

    def visit_SetComp(self, node: ast.SetComp) -> ast.SetComp:
        """
        Visit a set comprehension.
        
        Set comprehensions can contain comprehensions and have their own scope.
        """
        # Enter set comprehension scope
        self._enter_scope()
        
        # Process set comprehension
        node.elt = self.visit(node.elt)
        node.generators = [self.visit(gen) for gen in node.generators]
        
        # Exit set comprehension scope
        self._exit_scope()
        
        return node

    def visit_DictComp(self, node: ast.DictComp) -> ast.DictComp:
        """
        Visit a dictionary comprehension.
        
        Dict comprehensions can contain comprehensions and have their own scope.
        """
        # Enter dict comprehension scope
        self._enter_scope()
        
        # Process dict comprehension
        node.key = self.visit(node.key)
        node.value = self.visit(node.value)
        node.generators = [self.visit(gen) for gen in node.generators]
        
        # Exit dict comprehension scope
        self._exit_scope()
        
        return node

    def _rename_in_scope(self, name: str) -> str:
        """
        Rename a variable name within the current scope.
        
        Args:
            name: The original variable name.
            
        Returns:
            The obfuscated name for this variable.
        """
        # Get the current scope
        current_scope = self._get_current_scope()
        
        # If already renamed, return the existing mapping
        if name in current_scope:
            return current_scope[name]
        
        # Generate new name based on original name and scope depth
        obfuscated_name = self._generate_obfuscated_name(name, len(self.scopes) - 1)
        
        # Store mapping for future references
        current_scope[name] = obfuscated_name
        
        return obfuscated_name

    def visit_Name(self, node: ast.Name) -> ast.Name:
        """
        Visit a name node.
        
        Rename the name if it's a local variable (not builtin or imported).
        """
        # Only rename if it's a local variable that is not built-in or imported
        if isinstance(node.ctx, (ast.Store, ast.Load)) and self._is_local_name(node.id):
            # Rename only in local scope
            node.id = self._rename_in_scope(node.id)
            
        return node

    def visit_Attribute(self, node: ast.Attribute) -> ast.Attribute:
        """
        Visit an attribute node.
        
        Attributes (like obj.method) should not be renamed since they refer to identifiers
        that are likely not local variables. However, we need to process their value.
        """
        # Process the object part of the attribute access
        node.value = self.visit(node.value)
        
        return node

    def visit_With(self, node: ast.With) -> ast.With:
        """
        Visit a with statement.
        
        With statements can have items that bind names (e.g., 'as var'), so we need to
        handle those properly within their scope.
        """
        # Enter with block scope
        self._enter_scope()
        
        # Process the with items and body
        node.items = [self.visit(item) for item in node.items]
        node.body = [self.visit(stmt) for stmt in node.body]
        
        # Exit with block scope
        self._exit_scope()
        
        return node

    def visit_WithItem(self, node: ast.WithItem) -> ast.WithItem:
        """
        Visit a with item.
        
        Process the context manager and the 'as' target variable if present.
        """
        node.context_expr = self.visit(node.context_expr)
        if node.optional_vars is not None:
            # Handle the 'as var' part
            node.optional_vars = self.visit(node.optional_vars)
            
        return node

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> ast.ExceptHandler:
        """
        Visit an except handler.
        
        Exception handlers can have a target name that binds to the exception object.
        """
        # Enter exception handler scope
        self._enter_scope()
        
        if node.name is not None:
            # Handle 'except Exception as e'
            self._rename_in_scope(node.name)
            
        # Process body of exception handler
        node.body = [self.visit(stmt) for stmt in node.body]
        
        # Exit exception handler scope
        self._exit_scope()
        
        return node


def obfuscate_file(input_path: str, output_path: str):
    """
    Obfuscate a Python source file.
    
    Args:
        input_path: Path to the input .py file.
        output_path: Path to the output obfuscated .py file.
        
    Raises:
        SyntaxError: If the input file has invalid syntax.
        IOError: If there's an issue reading or writing files.
    """
    try:
        # Read source code from input file
        with open(input_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Parse source code into AST
        tree = ast.parse(source_code)
        
        # Transform AST to rename variables
        renamer = VariableRenamer()
        transformed_tree = renamer.visit(tree)
        
        # Convert back to source code
        obfuscated_code = ast.unparse(transformed_tree)
        
        # Write obfuscated code to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
            
    except SyntaxError as e:
        raise SyntaxError(f"Invalid syntax in {input_path}: {e}")
    except IOError as e:
        raise IOError(f"File error: {e}")


def main():
    """Main entry point for the bug obfuscator."""
    if len(sys.argv) != 3:
        print("Usage: python bug_obfuscator.py <input.py> <output.py>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    try:
        obfuscate_file(input_file, output_file)
        print(f"Successfully obfuscated {input_file} -> {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
