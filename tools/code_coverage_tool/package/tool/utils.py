import subprocess

from ..util.setting import TestPlatform, TestType
from ..util.utils import print_error


def run_cpp_test(binary_file: str) -> None:
    # cpp test binary
    try:
        subprocess.check_call(binary_file)
    except subprocess.CalledProcessError:
        print_error(f"Binary failed to run: {binary_file}")


def get_tool_path_by_platform(platform: TestPlatform):
    if platform == TestPlatform.FBCODE:
        from ..fbcode.utils import get_llvm_tool_path

        return get_llvm_tool_path()
    else:
        from ..oss.utils import get_llvm_tool_path

        return get_llvm_tool_path()
