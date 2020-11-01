>1. DAO, DTO, VO에 대해 알아오세요.
>2. 본인 코드에서 DAO, DTO, VO 역할을 하는 부분을 찾으세요.

# DAO, DTO, VO

## 1. DAO (Data  Access Object)

Database의 data에 접근하는 객체

```python
from server import DATABASE_URL
engine = create_engine(DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
```

```python
user = session.query(User).filter(User.email == email).first()
```



## 2. DTO (Data Transfer Object)

데이터베이스 레코드의 데이터를 매핑하기 위한 데이터 객체

```python
class User(Base):
    __tablename__ = 'users'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    email = Column(String(30), primary_key=True)
    password = Column(String(100), nullable=False)
    nickname = Column(String(20), nullable=False)
    age = Column(INT, nullable=False)
    img = Column(String, nullable=True, default='user.jpg')
```

```python
new_user = User(email=email,
                password=generate_password_hash(password),
                nickname=nickname,
                age=age)
```

## 3. VO (Value Object)



