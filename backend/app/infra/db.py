from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接字符串（确保正确设置）
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/restaurant_analytics"

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# 创建 Base 类，所有模型需要继承它
Base = declarative_base()

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)