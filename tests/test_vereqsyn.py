import pathlib
import shutil

import pytest

from vereqsyn import VersionCfgRequirementsTxtSync, ConfigFile


@pytest.fixture(scope="session")
def fixtures() -> pathlib.Path:
    """Return a pathlib.Path to the fixtures directory."""
    return pathlib.Path(__file__).parent / "fixtures"


def tmp_copy(target: pathlib.Path, src: pathlib.Path) -> pathlib.Path:
    """Create a copy of ``src`` and return the new path."""
    shutil.copy(src, target)
    return target / src.name


def test_VersionCfg_RequirementsTxt_Sync___sync__1(fixtures, tmp_path):
    """It syncs newer versions in both directions."""
    r3 = tmp_copy(tmp_path, fixtures / "r3.txt")
    v3 = tmp_copy(tmp_path, fixtures / "v3.cfg")
    component = VersionCfgRequirementsTxtSync(r3, v3)
    assert not component.in_sync()
    component._sync()  # noqa: SLF001 Private member accessed
    assert component.in_sync()


def test_VersionCfg_RequirementsTxt_Sync___sync__2(fixtures):
    """It raises an exception if the package names are out of order."""
    component = VersionCfgRequirementsTxtSync(fixtures / "r1.txt", fixtures / "v2.cfg")
    with pytest.raises(ReferenceError) as err:
        component._sync()  # noqa: SLF001 Private member accessed
    assert str(err.value).startswith("Package entries out of order: Faker != FactoryBoy. Please recreate")


def test_VersionCfg_RequirementsTxt_Sync___recreate__1(fixtures, tmp_path):
    """It recreates requirements.txt from versions.cfg."""
    r1 = tmp_copy(tmp_path, fixtures / "r1.txt")
    v2 = tmp_copy(tmp_path, fixtures / "v2.cfg")
    component = VersionCfgRequirementsTxtSync(r1, v2)
    assert not component.in_sync()
    component._recreate()  # noqa: SLF001 Private member accessed
    assert component.in_sync()


def test_VersionCfg_RequirementsTxt_Sync__in_sync__1(fixtures):
    """It returns `True` if config files are in sync."""
    component = VersionCfgRequirementsTxtSync(requirements_txt=fixtures / "r1.txt", version_cfg=fixtures / "v1.cfg")
    assert component.in_sync()


@pytest.mark.parametrize(
    ("r_name", "v_name"),
    [
        ("r1.txt", "v1-min.cfg"),
        ("r1-min.txt", "v1.cfg"),
        ("r1.txt", "v2.cfg"),
        ("r1.txt", "v3.cfg"),
    ],
)
def test_VersionCfg_RequirementsTxt_Sync__in_sync__2(fixtures, r_name, v_name):
    """It returns `False` if config files are out of sync."""
    component = VersionCfgRequirementsTxtSync(requirements_txt=fixtures / r_name, version_cfg=fixtures / v_name)
    assert not component.in_sync()


def test_VersionCfg_RequirementsTxt_Sync__update__1(fixtures, tmp_path):
    """It updates out of sync files."""
    r3 = tmp_copy(tmp_path, fixtures / "r3.txt")
    v3 = tmp_copy(tmp_path, fixtures / "v3.cfg")
    component = VersionCfgRequirementsTxtSync(requirements_txt=r3, version_cfg=v3)
    assert not component.in_sync()
    component.update()
    assert component.in_sync()


def test_VersionCfg_RequirementsTxt_Sync__update__2(fixtures, tmp_path):
    """It recreates requirements.txt if packages are out of order."""
    r1 = tmp_copy(tmp_path, fixtures / "r1.txt")
    v2 = tmp_copy(tmp_path, fixtures / "v2.cfg")
    component = VersionCfgRequirementsTxtSync(requirements_txt=r1, version_cfg=v2)
    assert not component.in_sync()
    component.update()
    assert component.in_sync()

def test_ConfigFile____post_init____1():
    """It raises a ValueError, if the given file does not exist."""
    with pytest.raises(ValueError) as e:
        ConfigFile(pathlib.Path('i-do-not-exist.cfg'))
    assert e.match("PosixPath\('i-do-not-exist.cfg'\) does not exist\.")

