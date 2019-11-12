# Copyright Iris contributors
#
# This file is part of Iris and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.

# Import Iris tests first so that some things can be initialised before
# importing anything else.
import iris.tests as tests

from .extest_util import (
    add_examples_to_path,
    show_replaced_by_check_graphic,
    fail_any_deprecation_warnings,
)


class TestCrossSection(tests.GraphicsTest):
    """Test the cross_section example code."""

    def test_cross_section(self):
        with fail_any_deprecation_warnings():
            with add_examples_to_path():
                import cross_section
            with show_replaced_by_check_graphic(self):
                cross_section.main()


if __name__ == "__main__":
    tests.main()
