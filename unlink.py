import os
import shutil

from argparse import ArgumentParser


def _main() -> None:
    parser = ArgumentParser(description='Replaces symlinks with copies of their targets')
    parser.add_argument('--dir', required=True, help='Directory that contains symlinks')
    args = parser.parse_args()

    for e in sorted(os.listdir(args.dir)):
        element = os.path.join(args.dir, e)
        if not os.path.islink(element):
            continue
        source = os.path.realpath(element)
        print('{} -> {}'.format(e, source))
        os.remove(element)
        shutil.copytree(source, element)


if __name__ == '__main__':
    _main()
