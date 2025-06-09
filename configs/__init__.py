# Copyright 2025 Thousand Brains Project
#
# Copyright may exist in Contributors' modifications
# and/or contributions to the work.
#
# Use of this source code is governed by the MIT
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

from __future__ import annotations

from .experiments import CONFIGS as EXPERIMENT_CONFIGS

__all__ = ["CONFIGS"]

CONFIGS: dict[str, dict] = {}
CONFIGS.update(EXPERIMENT_CONFIGS)
