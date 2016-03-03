from sys import exit
import click
import requests


def check(url, text, verify):
    try:
        r = requests.get(url, verify=verify)

        if r.status_code != 200:
            click.echo('CRITICAL - bad status code')
            exit(2)
        else:
            if text:
                if text in r.text:
                    click.echo('OK')
                    exit(0)
                else:
                    click.echo('CRITICAL - could not find text')
                    exit(2)

            else:
                click.echo('OK')
                exit(0)

    except Exception as e:
        click.echo('CRITICAL - {}'.format(e))
        exit(2)


@click.command()
@click.argument('url')
@click.option('--text', default=None,
              help='Looking for text in response body.')
@click.option('--verify/--no-verify', default=True,
              help='Verify SSL certificate.')
def cli(url, text, verify):
    check(url, text, verify)
