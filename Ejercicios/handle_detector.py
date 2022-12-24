#!/usr/bin/env python3

try:
    import logging
    import os
    import pathlib
    import re
    import sys

except ImportError as error:
    print(error)

'''Handle detector  Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://" 
 *   y finalizan con un dominio (.com, .es...)'''

 ### Usando argumentos del sistema y ejecutandolo por threading


##Patterns
pattern_hash = r"^#.*"
pattern_user = r"^@.*"
pattern_web = r"^[https?://].*[.com | .es]$"
test = re.search(pattern=pattern_web, string=sys.argv[1])
print(test)


if __name__ == "__main__":
    pass
