#!/usr/bin/env python3

try:
    import logging
    import os
    import pathlib
    import re
    import sys
    from concurrent import futures

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
dictionary_patterns = {"Hash":pattern_hash, "User":pattern_user, "Web":pattern_web}

def detect_handle():
    detect_user = str(sys.argv[1])

    for key, value in dictionary_patterns.items():
        
        detector_hand = re.search(pattern=value, string=detect_user)

        if detector_hand != None:
            print(f"Handle: {key}")
            sys.exit(0)
        else:
            continue

    print("No handle detected")



if __name__ == "__main__":
    executor = futures.ThreadPoolExecutor()
    executor.submit(detect_handle)
    

