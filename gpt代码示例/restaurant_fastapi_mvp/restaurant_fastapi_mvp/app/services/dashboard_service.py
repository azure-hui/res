from app.core.errors import NotFoundException
from app.services.mock_data import MOCK_DASHBOARD_OVERVIEW


class DashboardService:
    @staticmethod
    def get_overview(store_id: str) -> dict:
        overview = MOCK_DASHBOARD_OVERVIEW.get(store_id)
        if not overview:
            raise NotFoundException("首页概览数据不存在")
        return overview
