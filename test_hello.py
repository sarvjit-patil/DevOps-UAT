
from hello import main

def test_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, DevOps UAT Environment!\n"
