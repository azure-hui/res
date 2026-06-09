from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.db.base_class import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.dashboard_snapshot import DashboardSnapshot
    from app.models.user_store_rel import UserStoreRel

class Store(Base):
    __tablename__ = "stores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    city: Mapped[str | None] = mapped_column(String(64), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    user_relations: Mapped[list["UserStoreRel"]] = relationship(
        back_populates="store",
        cascade="all, delete-orphan",
    )
    dashboard_snapshots: Mapped[list["DashboardSnapshot"]] = relationship(
        back_populates="store",
        cascade="all, delete-orphan",
    )
