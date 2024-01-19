import argparse

import vereqsyn


def main(argv=None):
    parser = argparse.ArgumentParser(
        "vereqsyn",
        "{prog} <version.cfg> <requirements.txt>",
        "Bi-directional version.cfg <-> requirements.txt synchronization",
    )
    parser.add_argument("version_cfg", action="store")
    parser.add_argument("requirements_txt", action="store")

    args = parser.parse_args(argv)
    command = vereqsyn.VersionCfgRequirementsTxtSync(args.requirements_txt, args.version_cfg)
    command.update()


if __name__ == "__main__":  # pragma: no cover
    main()
