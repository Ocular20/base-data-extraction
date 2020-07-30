The Fornax team will adhere to consistent quality coding practices, but also works to continuously improve those practices.
Unit tests are a must.

Table of Contents
[Conventions](#conventions)
[Private Functions](#private-functions)
[Code Formatting](#code-formatting)
[General](#general)
[Names](#names)
[Spaces](#spaces)
[Docstrings](#docstrings)
[Imports](#imports)
[Return Statements](#return-statements)
[Commands](#commands)
[Writing Tests](#writing-tests)
[Test Files](#test-files)
[Pytest Fixtures](#pytest-fixtures)
[Tests](#tests)
[Mocking](#mocking)
[Data Driven Tests](#data-driven-tests)
[Assertions](#assertions)
[Assertion Wrapper Functions](#assertion-wrapper-functions)

# Conventions
Private Functions
Python has no enforcement of private functions or methods.
By convention we define "private" functions and methods by prepending the function name with an underscore, e.g. def _my_sort_of_private_function(): and only call them from within the module they are defined in, (except in test code).
Although "private" functions can be called from outside of their module, they must not be (except in test code).
Any need to use a function in multiple modules means that it should be made "public" and if appropriate moved to a utils module.
As noted, in test code, private functions may be called from outside their module and it is common to do so.

# Code Formatting
General
We care about: Readability, Scalability and Maintainability. Specifically:

Remove all commented out code. (comments are fine, great actually, but defunct commented code is not)
Avoid compound statements unless it makes the code more readable. Just because you can do everything on a single line doesn't mean you should. 
Follow PEP 8.

# Names
Use snake_case for variable, function and method names

As per Python rules, use TitleCase (aka PascalCase) for class names.

Name functions and variables descriptively. Favor clarity over terseness, e.g.

Good

def _wait_for_resource_deletion() {

    # code here
}

Bad

def _wait4res_del() {

    # code here
}

# Spaces
Spaces for indenting code

🎊**Not tabs. Never tabs!**🎊
Each indent must be 4 spaces.
Spaces between operators. Got a '=' thats not part of a named argument? Put some white spaces around it. Got a '+'? He loves white spaces too. White space! White space for everyone!!

Good

def get_big_thing():

    thing       = 2
    other_thing = 3
    sum_thing   = thing + other_thing

    return thing * sum_thing

Bad

def get_big_thing():

    thing=2
    other_thing= 3

    sum_thing =thing+other_thing

    return thing* sum_thing
Two blank lines between top level definitions including classes and function definitions.

One blank line between method definitions within a class.

Rule of thumb with blank lines -

It is best to start each new block (indentation) with a blank line for separation.
It is generally acceptable to group statements on contiguous lines if they are similar or related and are aligned on operators. However, if in doubt, separate statements with blank lines for readability.
It is unacceptable to include excessive blank lines anywhere, i.e. 1 or 2 blank lines are good as described above, but there is not otherwise any reason to have 2 contiguous blank lines.
Good

def get_thing_length(param1):

    thing_length = 0

    thing_var_a = 'some value'
    thing_var_b = '{} {}'.format(thing_var_a, thing_var_b)

    if len(param1) > 5:

        thing_length = len(param1)

    if len(thing_var_b) > 20:

        thing_length = len(thing_var_c)

    return thing_length

Bad

def get_thing_length(param1):



    thing_length = 0

    thing_var_a = 'some value'
    thing_var_b = '{} {}'.format(thing_var_a, thing_var_b)
    if len(param1) > 5:
        thing_length = len(param1)

    if len(thing_var_b) > 20:
        thing_length = len(thing_var_c)
    return thing_length

# Docstrings

Note: Clear, well written and easy to understand code is greatly favored over the use of docstrings
Docstrings are optional and may be used to add clarity to the purpose and functioning of modules, methods and functions.
When writing a docstring, refer to the following for guidance:
    Method/Function Docstring
       Method/Function description: Here you can provide in plain language (hopefully one everyone you are working with understands) what the thing does.
       Parameter descriptions: Include a description of each parameter. In the best cases these descriptions will include the type of the parameter and its overall purpose.
    Class Docstring
        Description of your class and its purpose.
    Module Dostring
        General description of the modules purpose. You can be as fancy or abbreviated as you want. If you desire glory, fortune and fame you can put your author tag here.

For method signature definitions in docstrings use the style outlined in the Sphinx Documentation.

# Imports

Imports should be grouped in the following fashion.
    All standard library imports should come before third party imports. e.g. import os should come before import requests
    All simple (or "vanilla") import statements should precede all from ... import statements.
    Group like imports, e.g. group multiple imports from the same module, group single imports from distinct modules (see example below)

In most cases, import specific functions from modules rather than just importing the whole module.

Good

import dateutil.parser
import re

from datetime import datetime
from datetime import timedelta

from munch import munchify
from shade import simple_logging
from aenum import Enum

from file_name.function_name_1 import get_cloud
from file_name.function_name_2 import list_stacks

Bad

import dateutil.parser
import re
from file_name.function_name_1
from datetime import datetime
import shade
import aenum
from datetime import timedelta
from munch import munchify

# Return Statements
Generally, return statements should be simple and short.

    Return statements may include simple computation, e.g.
    return "{}/{}".format(param1, param2)

    Return statements may include more sophisticated computation if not doing so would only save 1 line of code and require another variable due to the use of inherently (relatively) complex functions, e.g.
    return list(filter(lambda r: not any(exclusion.match(r[key_name]) for exclusion in exclude_patterns)), resources)

There should be only 1 return statement in a function or method.

Good

def get_the_thing_we_want(some_other_thing):

    the_thing_we_want = null

    if (meets_some_condition(some_other_thing)):

        the_thing_we_want = 'something'

    return the_thing_we_want

Bad

def get_the_thing_we_want(some_other_thing):

    if (meets_some_condition(some_other_thing)):

        return 'something'

    else:

        return None


# Writing Tests
Every module must have tests for every function, method and constant.

Integration Tests
test_[command_name]_int.py

#### Unit Tests
We use unit tests to validate the behavior of functions and methods, and the values constants.
    Unit tests should be (by far) the most numerous tests written in relation to any component code.
    All unit tests must go into the tests/unit directory and be named in the following fashion:
    test_[module_name].py

We use the pytest framework and the unittest library for test automation.

    We prefer pytest -- fixtures rather than setUp methods.
    We prefer top-level test methods rather than class test methods.
    Avoid repetitive literals within tests. Use test level variables.
    Avoid repetitive literals across tests. Use constants at the top level of the test files.

We generally do not do "strict mocking", i.e. unexpected calls on mock objects are allowed.

For the most part, test code style should adhere to all of the same rules as regular code.

# Test Files
All test files must adhere to the following pattern:

Files start with Imports organized in the fashion described in the imports section of this document
Constants are declared after the import statements.
Fixtures should be placed after constants and before test methods.
Good

"""
Optional Test module level docstring goes here
"""

import complete_standard_library_modules_here

import complete_third_party_modules_here

from third_party_modules import specific_functions here

from local_module_under_test import specific_functions_under_test_here


CONSTANTS_GO_HERE = dateutil.parser.parse(SOME_IMPORTED_OR_DECLARED_CONSTANT).tzinfo


@pytest.fixture
def dummy_resources_list():

    list = [
        DUMMY_RESOURCE_CREATED_ON_EPOCH,
        DUMMY_RESOURCE_CREATED_AFTER_EPOCH,
        DUMMY_RESOURCE_CREATED_BEFORE_EPOCH
    ]

    return list


# Tests
Very simple tests can be written very simply, e.g.

def make_prunable_resource_assertions(self, prunable_resources):

    # expect
    self.assertEqual(1, len(prunable_resources))
    self.assertTrue(all(map(lambda s: s["prunable"], prunable_resources)))
Most other tests should include some form of given, when, then, given, expect or just expect formatting, e.g.

def test_connection_retry_limit_constant(test_case):

    # expect
    test_case.assertEqual(CONNECTION_RETRY_LIMIT, 5)
def test_get_connection_raises_exception(test_case, dummy_environment):

    # given
    del dummy_something[SOME_VAR]

    # expect
    with patch.dict("file.path.in.repo", values=xyz, clear=True):
        with test_case.assertRaisesRegex(CredentialNotFoundException, EXCEPTION_MSG):
            function_to_test()

In general when asserting that a mock was called, favor the use of assert_called_once_with or assert_called_with over assert_called_once

# Mocking
It is often necessary to mock functions being called by the unit under test. The 'with patch' pattern for mocking must always be used rather than using a patch decorator, e.g.

Good

def test_image_reap(self):

      # Given

      with patch("path.to.file.function_name", side_effect=dummy_resources_list):
          with patch("path.to.file.function_name") as mock_something:
              _fuinction_to_unit_test(x, [], y, DEFAULT_TIMEOUT, False, DEBUG)

      # Expect

      mock_something.assert_called_once_with(DUMMY_RESOURCE_CREATED_BEFORE_EPOCH["name"],
                                                    timeout=DEFAULT_TIMEOUT,
                                                    debug=DEBUG)

Bad

@patch('package.module.attribute', mock.attribute)
def test():

    from package.module import attribute

    assert attribute is mock.attribute

Bad

@patch.object(SomeClass, 'static_method')
def test_something(self, mock_method):

    SomeClass.static_method()

    mock_method.assert_called_with()

# Data Driven Tests
To accomplish data driven tests, use the [mark.parametrize] decorator, e.g.

@pytest.mark.parametrize("exception, expected", [[requests.exceptions.ConnectionError(), True], [Exception(), False]])
def test_retry_if_connection_error(test_case, exception, expected):

    # when
    actual = _retry_if_connection_error(exception)

    # then
    test_case.assertEqual(actual, expected)

# Assertions
When asserting on exceptions, use assertRaisesRegex to assert on the exception message content rather than assertRaises that only asserts that any exception was raised.

# Assertion Wrapper Functions
In some test files, multiple tests will use the same assertions that can be extracted out into functions that wrap the actual assertions.

This should be done with the aim of less duplicated code and easier to read tests.
Tests utilizing this approach should not group calls to an assertion wrapper within one test as it makes failures more difficult to understand.
Good

def _run_test_with_versions(self, versions, latest_expected):

      # when
      latest_actual = get_latest_semver_release(versions)

      # then
      if latest_expected is None:
          self.assertIsNone(latest_actual)
      else:
          self.assertEqual(latest_actual, latest_expected)

def test_get_latest_semver_release_no_versions(self):

      self._run_test_with_versions([], None)

def test_get_latest_semver_release_no_release_versions(self):

      self._run_test_with_versions([ "foo", "1.2.3-rc4", "" ], None)

Bad

def _run_test_with_versions(self, versions, latest_expected):

      # when
      latest_actual = get_latest_semver_release(versions)

      # then
      if latest_expected is None:
          self.assertIsNone(latest_actual)
      else:
          self.assertEqual(latest_actual, latest_expected)

def test_get_latest_semver_release_many_release_versions(self):

      # difference in major
      self._run_test_with_versions([ "1.0.0", "2.0.0" ], "2.0.0")
      self._run_test_with_versions([ "2.0.0", "1.0.0" ], "2.0.0")
      self._run_test_with_versions([ "2.0.0", "11.0.0" ], "11.0.0")

      # difference in minor
      self._run_test_with_versions([ "1.0.0", "1.1.0" ], "1.1.0")
      self._run_test_with_versions([ "1.1.0", "1.0.0" ], "1.1.0")
      self._run_test_with_versions([ "1.2.0", "1.11.0" ], "1.11.0")

      # difference in patch
      self._run_test_with_versions([ "1.0.0", "1.0.1" ], "1.0.1")
      self._run_test_with_versions([ "1.0.1", "1.0.0" ], "1.0.1")
      self._run_test_with_versions([ "1.0.2", "1.0.11" ], "1.0.11")

