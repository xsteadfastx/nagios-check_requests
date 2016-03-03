from click.testing import CliRunner
import pytest
import responses
import requests

from check_requests.cli import cli


@pytest.mark.parametrize('status_code,exit_code,output', [
    (200, 0, 'OK\n'),
    (404, 2, 'CRITICAL - bad status code\n')
])
@responses.activate
def test_status_code(status_code, exit_code, output):
    responses.add(responses.GET,
                  'http://foo.bar',
                  status=status_code)

    runner = CliRunner()
    result = runner.invoke(cli, ['http://foo.bar'])

    assert result.exit_code == exit_code
    assert result.output == output


@pytest.mark.parametrize('exit_code,body,text,output', [
    (0, 'Dies ist ein Test', 'Test', 'OK\n'),
    (2, 'Dies ist ein Test', 'foo', 'CRITICAL - could not find text\n')
])
@responses.activate
def test_text(exit_code, body, text, output):
    responses.add(responses.GET,
                  'http://foo.bar',
                  status=200,
                  body=body)

    runner = CliRunner()
    result = runner.invoke(cli, ['http://foo.bar', '--text', text])

    assert result.exit_code == exit_code
    assert result.output == output


@responses.activate
def test_exception():
    responses.add(responses.GET,
                  'http://foo.bar',
                  body=requests.exceptions.HTTPError('this is a exception'))

    runner = CliRunner()
    result = runner.invoke(cli, ['http://foo.bar'])

    assert result.exit_code == 2
    assert result.output == 'CRITICAL - this is a exception\n'
