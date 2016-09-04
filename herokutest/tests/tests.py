def test_layout_h1(testapp):
    assert testapp.get('/').html.find('h1')


def test_layout_response(testapp):
    assert testapp.get('/').html.find(attrs={'id': 'response'})


def test_layout_404(testapp):
    assert testapp.get('/heck', status=404)


def test_layout_bad_address(testapp):
    assert 'bad address' in testapp.get('/?address=heck')
