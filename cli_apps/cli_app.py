import click
import utils.helper_functions as helper_functions


@click.command()
@click.option("--first_val", prompt="first_val", help="The first value to add")
@click.option("--second_val", prompt="second_val", help="The second value to add")
def add_x(first_val: float, second_val: float):
    result = helper_functions.add_x(float(first_val), float(second_val))
    click.echo(result)


if __name__ == "__main__":
    add_x()