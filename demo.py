import subprocess

output = subprocess.check_output("python dummy.py")
output1 = output.decode()
output2 = output1.split("\n")



def test_multiply():
    output3 = output2[8].rstrip("\r")
    assert output3 == "11 X 9 = 99"


def test_dummy():
    assert "110" in output1


