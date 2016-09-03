def test_root(testapp):
    assert testapp.get('/'), str
