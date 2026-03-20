from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class UserEvent(BaseModel):
    user_id: str = Field(..., description="Unique ID of the user")
    event_type: str = Field(..., description="Type of activity (view_product, purchase, etc.)")
    product_id: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class EventResponse(BaseModel):
    status: str
    message: str
    event_id: str
