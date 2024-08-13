# Logging Module

import logging

# -----------------------------------------------
# <<<<yeh just short project k liay sahi hai>>>>
#     yeh just one time k liay acha hai
#    aghr humay just ek quick setup krna ho
# -----------------------------------------------
# basic logging steps
# hum iss may console k liay log nahi bana sakhte
logging.basicConfig(level=logging.DEBUG, filename= "my_log.log", format= "%(asctime)s - "
                    "%(levelname)s - %(message)s")

logging.debug("I am 'Debugging' Logging")
logging.info("I am 'Information' Logging")
logging.warning("I am 'Warning' Logging")
logging.error("I am 'Error' Logging")
logging.critical("I am 'Critical' Logging")


# now we will create log for both console and file
# -----------------------------------------------
# <<<<yeh just largest project k liay sahi hai>>>>
#     yaha hum mutiple times use kr sakhte hai
# matlab hum multiple times custom handlers aur formattors define kr k use sakhte hai
# -----------------------------------------------

logger = logging.getLogger("strong_logger")

logger.setLevel(logging.DEBUG)  # Log level set karta hai, taake saare levels ke messages log ho sakein

# Formatter create karta hai jo log messages ko specified format me represent karega
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

console_handle = logging.StreamHandler()  # Stream handler for console
console_handle.setLevel(logging.DEBUG)  # yeh saare level set karta ha

file_handle = logging.FileHandler("logger_file.log")  # File handler for logging file
file_handle.setLevel(logging.DEBUG)  # yeh saare level set karta ha

# yaha hum nay banaya gaya formatter jss ka name "formatter" hai, set kr rahe hai inn dono pr
# ek console pr set kara hai
console_handle.setFormatter(formatter)
# ek file pr set kara hai
file_handle.setFormatter(formatter)

logger.addHandler(console_handle)
logger.addHandler(file_handle)
# yaha kuch simple function banaey hai, log pr astamaal krne k liay
def sum(a, b):
    return a + b

def full_name(f_name, l_name):
    return f_name, l_name

def divide():
    try:
        return 10 / 0
    except Exception as e:
        logger.error("can not divide with zero value")

# yaha hum log messages set kr rahe hai k kiya display krwana hai 'file' ya 'console' pr
logger.debug(sum(10, 100))
logger.info(full_name("Noman", "Aslam"))
divide()
logger.warning("this is warning message")
logger.critical("this is critical message ")