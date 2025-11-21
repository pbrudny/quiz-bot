from main import main, hello

def test_hello():
    assert hello() == "Hello, World!"

def test_main_prints_message(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello from quiz-bot!"
