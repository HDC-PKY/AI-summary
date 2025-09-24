"""프로젝트 전반에서 사용되는 유틸리티 클래스 및 함수 모음."""
from __future__ import annotations

import sys
import threading
import time

from .logging import get_logger
from .paths import resolve_repo_root


class StartupSpinner:
    """아주 이른 단계부터 '살아있음'을 보여주는 콘솔 스피너."""

    FRAMES = ["|", "/", "-", "\\"]

    def __init__(self, prefix: str = "", interval: float = 0.15) -> None:
        self.prefix = prefix
        self.interval = interval
        self._stop = threading.Event()
        self._t = None
        self._i = 0

    def start(self) -> None:
        if self._t:
            return

        def _run() -> None:
            while not self._stop.wait(self.interval):
                frame = self.FRAMES[self._i % len(self.FRAMES)]
                self._i += 1
                sys.stdout.write(f"\r{self.prefix} {frame} ")
                sys.stdout.flush()

        self._t = threading.Thread(target=_run, daemon=True)
        self._t.start()

    def stop(self, clear_line: bool = True) -> None:
        if not self._t:
            return
        self._stop.set()
        self._t.join()
        if clear_line:
            sys.stdout.write("\r" + " " * 80 + "\r")
            sys.stdout.flush()


__all__ = ["StartupSpinner", "get_logger", "resolve_repo_root"]
