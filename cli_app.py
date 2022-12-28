import click


@click.command()
@click.option("--first_val", prompt="first_val", help="The first value to add")
@click.option("--second_val", prompt="second_val", help="The second value to add")
def add_x(first_val, second_val):
    result = first_val + second_val
    click.echo(result)


if __name__ == "__main__":
    add_x()
