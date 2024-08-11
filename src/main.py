input_path = "/home/cryptid/workspace/github.com/cryptidcodes/static_site_generator/static"
output_path = "/home/cryptid/workspace/github.com/cryptidcodes/static_site_generator/public"

# PROGRAM IS FUNCTIONAL - MAYBE SOME SMALL TIDYING TO DO
# REMOVE PRINT STATEMENTS, LEAVE BETTER FN DESCRIPTIONS ETC
# ALSO REWORK ABSOLUTE FILEPATHS TO RELATIVE

########################################################################

import os
import shutil

from generate_page import generate_pages_recursive

def copydir(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    if os.path.isfile(src):
        shutil.copy(src, dst)
    elif os.path.isdir(src):
        if not os.path.exists(dst):
            os.mkdir(dst)
        for object in os.listdir(src):
            copydir(os.path.join(src, object), os.path.join(dst, object))
    else:
        raise Exception("ERROR:: Unexpected Path")

def main():
    copydir(input_path, output_path)
    generate_pages_recursive(
        "/home/cryptid/workspace/github.com/cryptidcodes/static_site_generator/content",
        "/home/cryptid/workspace/github.com/cryptidcodes/static_site_generator/template.html",
        "/home/cryptid/workspace/github.com/cryptidcodes/static_site_generator/public"
        )
main()