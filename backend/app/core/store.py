from datetime import date


class MemoryStore:
    def __init__(self) -> None:
        self.levels = {
            1: {
                "id": 1,
                "name": "普通会员",
                "min_points": 0,
                "discount": 1.0,
                "benefits": ["积分累计", "新品提醒"],
            },
            2: {
                "id": 2,
                "name": "银卡会员",
                "min_points": 500,
                "discount": 0.95,
                "benefits": ["95折优惠", "生日双倍积分"],
            },
            3: {
                "id": 3,
                "name": "金卡会员",
                "min_points": 1500,
                "discount": 0.9,
                "benefits": ["9折优惠", "预售优先购", "专属推荐"],
            },
        }
        self.members = {
            1: {
                "id": 1,
                "name": "李明",
                "phone": "13800000001",
                "level_id": 2,
                "points": 860,
                "favorite_categories": ["柑橘", "莓果"],
            },
            2: {
                "id": 2,
                "name": "王芳",
                "phone": "13800000002",
                "level_id": 3,
                "points": 2100,
                "favorite_categories": ["热带水果", "礼盒"],
            },
        }
        self.rewards = {
            1: {
                "id": 1,
                "title": "10元水果券",
                "points_cost": 300,
                "stock": 24,
                "description": "满39元可用，适合日常补货。",
            },
            2: {
                "id": 2,
                "title": "精品蓝莓一盒",
                "points_cost": 680,
                "stock": 10,
                "description": "125g装，门店自提。",
            },
            3: {
                "id": 3,
                "title": "当季果篮升级",
                "points_cost": 1200,
                "stock": 8,
                "description": "果篮增加进口奇异果和车厘子。",
            },
        }
        self.presales = {
            1: {
                "id": 1,
                "title": "云南高山蓝莓预售",
                "fruit_name": "高山蓝莓",
                "price": 39.9,
                "original_price": 49.9,
                "start_date": date(2026, 6, 1),
                "end_date": date(2026, 6, 15),
                "pickup_date": date(2026, 6, 18),
                "quota": 200,
                "reserved": 68,
            },
            2: {
                "id": 2,
                "title": "海南贵妃芒礼盒",
                "fruit_name": "贵妃芒",
                "price": 88.0,
                "original_price": 108.0,
                "start_date": date(2026, 6, 5),
                "end_date": date(2026, 6, 20),
                "pickup_date": date(2026, 6, 23),
                "quota": 120,
                "reserved": 35,
            },
        }
        self.fruits = {
            1: {
                "id": 1,
                "name": "阳光玫瑰葡萄",
                "category": "葡萄",
                "freshness_score": 98,
                "origin": "云南",
                "price": 29.9,
                "tags": ["高甜", "无籽", "冷链到店"],
            },
            2: {
                "id": 2,
                "name": "佳沛金奇异果",
                "category": "进口水果",
                "freshness_score": 95,
                "origin": "新西兰",
                "price": 8.8,
                "tags": ["维C", "早餐", "会员热购"],
            },
            3: {
                "id": 3,
                "name": "泰国金枕榴莲",
                "category": "热带水果",
                "freshness_score": 92,
                "origin": "泰国",
                "price": 42.0,
                "tags": ["香甜", "预售同款", "高客单"],
            },
            4: {
                "id": 4,
                "name": "四川爱媛橙",
                "category": "柑橘",
                "freshness_score": 96,
                "origin": "四川",
                "price": 16.9,
                "tags": ["多汁", "家庭装", "复购高"],
            },
        }
        self.point_records = [
            {
                "id": 1,
                "member_id": 1,
                "change": 120,
                "type": "earn",
                "note": "购买当季水果",
                "created_at": "2026-06-01 10:00",
            },
            {
                "id": 2,
                "member_id": 2,
                "change": -300,
                "type": "redeem",
                "note": "兑换10元水果券",
                "created_at": "2026-06-01 11:30",
            },
        ]
        self.presale_orders = []

    def next_id(self, bucket: dict[int, dict]) -> int:
        return max(bucket.keys(), default=0) + 1

    def next_record_id(self) -> int:
        return len(self.point_records) + 1

    def next_order_id(self) -> int:
        return len(self.presale_orders) + 1


store = MemoryStore()
