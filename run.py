# Copyright 2025 Thousand Brains Project
#
# Copyright may exist in Contributors' modifications
# and/or contributions to the work.
#
# Use of this source code is governed by the MIT
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Entrypoint for running an experiment."""

from tbp.monty.frameworks.run_env import setup_env

setup_env()

from tbp.monty.frameworks.run import main  # noqa: E402

# Load all experiment configurations from local project.
from configs.experiments import CONFIGS  # noqa: E402

if __name__ == "__main__":
    main(all_configs=CONFIGS)
