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


class TestSOIFiltering(tests.GraphicsTest):
    """Test the SOI_filtering example code."""

    def test_soi_filtering(self):
        with fail_any_deprecation_warnings():
            with add_examples_to_path():
                import SOI_filtering
            with show_replaced_by_check_graphic(self):
                SOI_filtering.main()


if __name__ == "__main__":
    tests.main()
