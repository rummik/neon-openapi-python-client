{ pkgs, ... }:

{
  # https://devenv.sh/reference/options/
  packages = [];

  dotenv = {
    enable = true;
  };

  languages = {
    python = {
      enable = true;
      package = pkgs.python312;
      venv = {
        enable = true;
        requirements = ./requirements.txt;
      };
    };
  };

  enterTest = /* sh */ ''
    pylint -rn -sn \
      --generated-members=client.tasks,client.projects \
      --disable=logging-fstring-interpolation,import-error \
      $(git ls-files '*.py')

    python -m pytest -v
  '';
}
