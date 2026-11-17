
"""Privacy-first Rius tracing. No telemetry is sent without RIUS_API_KEY."""

import os
import logging

log = logging.getLogger(__name__)


def initialize():
    """Initialize observability if configured."""
    from dotenv import load_dotenv

    load_dotenv()

    if (
        not os.getenv("RIUS_API_KEY")
        or os.getenv("RIUS_DISABLED", "false").lower() in ("1", "true", "yes")
    ):
        log.info("Rius observability disabled")
        return

    try:
        import rius

        rius.init(
            service_name=os.getenv("RIUS_SERVICE_NAME", "atlas-ai-fde"),
            capture_content=False
        )

        log.info("Rius observability enabled")

    except Exception:
        log.exception("Rius initialization failed")


def trace(name):
    """Decorator for tracing functions without capturing inputs or outputs."""

    def decorate(fn):
        try:
            import rius

            return rius.observe(
                name=name,
                capture_input=False,
                capture_output=False
            )(fn)

        except ImportError:
            return fn

    return decorate
