from dataclasses import dataclass
from datetime import datetime

@dataclass
class GameEvent:
    action: str = ""
    timestamp: datetime = datetime.now()