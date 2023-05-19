import click
from const import CONFIG_FILE
from helper.rw import read_data_from_config, write_output
from helper.rw import read_config, generate_config_from_source_target
from helper.data_processing import sanitize_data, generate_and_show_stat


@click.command()
@click.option('--source', '-s', help='input filepath')
@click.option('--target', '-t', help='output filename')
def main(source: str=None, target: str=None):

    # read config
    if source and target:
        print(f"Reading config from cli arguments...")
        config = generate_config_from_source_target(source, target)
    else:
        print("Reading config from file...")
        config = read_config(CONFIG_FILE)

    # read data
    data = read_data_from_config(config)

    # transform data
    data = sanitize_data(data)

    # write output
    write_output(config, data)

    # show stats
    generate_and_show_stat(data)


if __name__ == '__main__':
    main()
