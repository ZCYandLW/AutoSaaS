/*
创建一个数据库saas
*/
# create database saas;

/*
创建动力类型表
*/
create table if not exists power_type(
  id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '动力类型',
  PRIMARY KEY ( id )
);

/*
创建市场级别
*/
create table if not exists market_level(
  id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '市场级别及细分级别',
  PRIMARY KEY ( id )
);

/*
创建档次等级
*/
create table if not exists grade_level(
  id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '档次等级',
  PRIMARY KEY ( id )
);

/*
创建车型血缘
*/
create table if not exists blood_relationship(
  id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '车系血缘',
  PRIMARY KEY ( id )
);

/*
创建车身类型
*/
create table if not exists car_type(
  id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '车身类型',
  PRIMARY KEY ( id )
);

/*
创建车企品牌
*/
create table if not exists car_brand(
  id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '车企品牌',
  PRIMARY KEY ( id )
);

/*
创建厂家名称表
*/
create table if not exists manufacturer_name(
  id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '厂家名称',
  PRIMARY KEY ( id )
);

/*
创建车辆属性表
*/
create table if not exists car(
  car_id int not null AUTO_INCREMENT,
  name VARCHAR(20)  comment '汽车名称',
  manufacturer_name_id int,
  car_brand_id int,
  power_type_id int,
  market_level_id int,
  grade_level_id int,
  blood_relationship_id int,
  car_type_id int,
  PRIMARY KEY ( car_id ),
  foreign key(manufacturer_name_id) references manufacturer_name(id),
  foreign key(car_brand_id) references car_brand(id),
  foreign key(power_type_id) references power_type(id),
  foreign key(market_level_id) references market_level(id),
  foreign key(grade_level_id) references grade_level(id),
  foreign key(blood_relationship_id) references blood_relationship(id),
  foreign key(car_type_id) references car_type(id)
);


/*
创建地理区域表
*/
create table if not exists  region(
    id int not null AUTO_INCREMENT  comment '区域id',
    name VARCHAR(20) comment '区域名称',
    PRIMARY KEY ( id )
);

/*
创建地理-省份表
*/
create table if not exists  province(
    id int not null AUTO_INCREMENT  comment '省份id',
    name VARCHAR(20) comment '省份名称',
    region_id int comment '区域id',
    PRIMARY KEY ( id ),
    foreign key(region_id) references region(id)
);

/*
创建地理-城市表
*/
create table if not exists  city(
    id int not null AUTO_INCREMENT  comment '城市id',
    region_id int comment '区域id',
    province_id int comment '省份id',
    name VARCHAR(20) comment '城市名称',
    PRIMARY KEY ( id ),
    foreign key(region_id) references region(id),
    foreign key(province_id) references province(id)
);

/*
创建地理-县市行政区表
*/
create table if not exists  district(
    id int not null AUTO_INCREMENT  comment '县市行政区id',
    name VARCHAR(20) comment '县市行政区名称',
    region_id int comment '区域id',
    province_id int comment '省份id',
    city_id int comment '城市id',
    PRIMARY KEY ( id ),
    foreign key(region_id) references region(id),
    foreign key(province_id) references province(id),
    foreign key(city_id) references city(id)
);


/*
创建基于城市的汽车关注人数数量表
*/
create table if not exists city_people_num(
    data_time DATE comment '时间',
    province_id VARCHAR(20) comment '省份id',
    city_id  VARCHAR(20)  comment '城市id',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( data_time, province, city ),
    foreign key(province_id) references province(id),
    foreign key(city_id) references city(id)
);

/*
创建汽车名称关注人数表
*/
create table if not exists car_interest_loophole(
    data_time DATE comment '时间',
    city_id int comment '城市id',
    car_id int comment '汽车id',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( data_time, city_id, car_id),
    foreign key(city_id) references city(id),
    foreign key(car_id) references car(id)
);


/*
创建经销商页面用户访问日志表
*/
create table if not exists user_logger(
    data_time datetime  comment '首次登陆时间',
    user_ip VARCHAR(20) comment '用户ip',
    car_dealer  VARCHAR(20)  comment '汽车经销商',
    is_call_phone int(2) default 0  comment '是否打电话',
    is_leave_clue int(2) default 0 comment '是否留下线索',
    PRIMARY KEY ( data_time, car_dealer, user_ip ),
    foreign key(car_dealer) references car_dealer(name)
);

/*
创建用户寻价记录表
*/
create table if not exists asking_low_price(
    data_time datetime comment '询价时间',
    user_ip VARCHAR(20) comment '用户ip',
    car_dealer  VARCHAR(20)  comment '汽车经销商',
    user_name int(2) default 0  comment '用户名称',
    user_phone int(2) default 0 comment '用户电话',
    PRIMARY KEY ( data_time, car_dealer, user_ip ),
    foreign key(car_dealer) references car_dealer(name)
);


/*
创建用户预约试驾表
*/
create table if not exists test_drive(
    data_time datetime comment '预约试驾时间',
    user_ip VARCHAR(20) comment '用户ip',
    car_dealer  VARCHAR(20)  comment '汽车经销商',
    user_name int(2) default 0  comment '用户名称',
    user_phone int(2) default 0 comment '用户电话',
    PRIMARY KEY ( data_time, car_dealer, user_ip ),
    foreign key(car_dealer) references car_dealer(name)
);

/*
创建经销商信息表
*/
create table if not exists car_dealer(
    dealer_id int not null AUTO_INCREMENT,
    name DATE comment '经销商名称',
    address TEXT comment '经销商地址',
    province_id VARCHAR(20) comment '经销商所在的省份id',
    city_id  VARCHAR(20)  comment '经销商所在的城市id',
    phone_num VARCHAR(20) comment '汽车经销商页面电话号码',
    visitor_num int comment '经销商总页面浏览人数',
    call_phone_num int comment '经销商总拨打电话人数',
    buy_num int comment '经销商总提供线索买车人数',
    PRIMARY KEY ( dealer_id ),
    foreign key(province_id) references province(id),
    foreign key(city_id) references city(id)
);


/*
创建经销商与车型关系表
*/
create table if not exists dealer_and_cars(
    id int not null AUTO_INCREMENT,
    dealer_id int  comment '经销商id',
    car_id int  comment '汽车id',
    PRIMARY KEY ( id ),
    foreign key(dealer_id) references car_dealer(dealer_id),
    foreign key(car_id) references car(car_id)
);



/*
创建经销商车型营销页面访问表
*/
create table if not exists car_sales_summary(
    id int not null AUTO_INCREMENT,
    data_time DATE comment '时间',
    dealer_car_id int  comment '经销商与汽车关系id',
    visitor_num int comment '车型营销页面页面浏览人数',
    call_phone_num int comment '拨打电话人数',
    buy_num int comment '提供线索买车人数',
    PRIMARY KEY ( data_time, dealer_car_id ),
    foreign key(dealer_car_id) references dealer_and_cars(id)
);

/*
创建经销商具体车型销售明细列表(如2018精英版)
*/
create table if not exists car_sales_details(
    id int not null AUTO_INCREMENT,
    name VARCHAR(20) comment '具体车型款式名称',
    naked_car_price float comment '具体车型裸车价(万)',
    guidance_price float comment '具体车型指导价(万)',
    dealer_id int  comment '经销商id',
    car_id int  comment '汽车id',
    PRIMARY KEY ( id ),
    foreign key(dealer_id) references car_dealer(dealer_id),
    foreign key(car_id) references car(car_id)
);


/*
创建活动计划投放表
*/
create table if not exists activity_plan(
    id int not null AUTO_INCREMENT,
    dealer_id int not null comment '经销商id',
    create_plan_time datetime comment '计划创建时间',
    activity_name int comment '活动名称',
    city_id int comment '城市id',
    district_id int comment '县市行政区id',
    plan_status tinyint comment '计划状态，0表示未发送，1表示已开始,2表示结束执行',
    push_mode int comment '推送模式,1代表短信,2代表精准营销,3代表云呼',
    watch_start_time date comment '看车周期开始时间',
    watch_end_time date comment '看车周期结束时间',
    intention_attributes VARCHAR(20) comment '意向属性，主要包括关注、兴趣、意向、到店',
    sexs tinyint unsigned comment '性别属性，采用二进制表示，第一位表示女01,第二位表示男10,即全部不选为0，女为1，男为2，,共4个值',
    ages tinyint unsigned comment '年龄属性，采用二进制表示，第一位表示小于25岁，第二位表示25~32岁，第三位表示32~40岁，第四位表示40~50岁，第五位表示大于50',
    cars text comment '选择车型,车名用;分割',
    push_freq tinyint comment '推送频次',
    time_interval int comment '时间间隔，单位为天',
    start_push_with_workingday time comment '工作日推送开始时间',
    end_push_with_workingday time comment '工作日推送结束时间',
    start_push_with_holiday time comment '节假日推送开始时间',
    end_push_with_holiday time comment '节假日推送结束时间',
    push_cover_num int comment '发送覆盖人数',
    push_cover_percent int comment '覆盖百分比，单位为%',
    PRIMARY KEY ( id ),
    foreign key(district_id) references district(id),
    foreign key(city_id) references city(id)
);

/*
第一张表：
创建一级统计表
多列索引适合多列同时查询，同时遵循最左前缀原则
单列索引适合单列查询
*/
create table if not exists one_level_statistics(
    id INT NOT NULL AUTO_INCREMENT,
    data_time DATE comment '时间',
    province VARCHAR(20) comment '省份',
    city  VARCHAR(20)  comment '城市',
    district VARCHAR(20)  comment '行政区',
    power_type VARCHAR(20)  comment '动力类型',
    child_field_name VARCHAR(20)  comment '子字段名称,主要包括车身类型、市场级别、细分级别、档次等级、车型品牌、厂家名称、车型血缘',
    child_field_value VARCHAR(20)  comment '子字段值，需要和子字段',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( id ),
    INDEX  child_field ( data_time, city, child_field_name, child_field_value, power_type)
);


/*
第二张表：
创建市场级别统计表（市场级别和细分市场放在一起用market_level表示）
*/
create table if not exists market_level_statistics(
    id INT NOT NULL AUTO_INCREMENT,
    data_time DATE comment '时间',
    province VARCHAR(20) comment '省份',
    city  VARCHAR(20)  comment '城市',
    district VARCHAR(20)  comment '行政区',
    power_type VARCHAR(20)  comment '动力类型',
    market_level VARCHAR(20)  comment '市场级别',
    child_field_name VARCHAR(20)  comment '子字段名称,主要包括车身类型、市场级别、细分级别、档次等级、车型品牌、厂家名称、车型血缘',
    child_field_value VARCHAR(20)  comment '子字段值，需要和子字段',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( id ),
    INDEX  child_field ( data_time, city, child_field_name, child_field_value, market_level, power_type)
);

/*
第三张表：
创建档次等级统计表
*/
create table if not exists grade_level_statistics(
    id INT NOT NULL AUTO_INCREMENT,
    data_time DATE comment '时间',
    province VARCHAR(20) comment '省份',
    city  VARCHAR(20)  comment '城市',
    district VARCHAR(20)  comment '行政区',
    power_type VARCHAR(20)  comment '动力类型',
    grade_level VARCHAR(20)  comment '档次等级',
    child_field_name VARCHAR(20)  comment '子字段名称,主要包括车身类型、市场级别、细分级别、档次等级、车型品牌、厂家名称、车型血缘',
    child_field_value VARCHAR(20)  comment '子字段值，需要和子字段',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( id ),
    INDEX  child_field ( data_time, city, child_field_name, child_field_value, grade_level, power_type)
);


/*
第四张表：
创建市场级别与档次等级关联统计表
*/
create table if not exists market_grade_level_statistics(
    id INT NOT NULL AUTO_INCREMENT,
    data_time DATE comment '时间',
    province VARCHAR(20) comment '省份',
    city  VARCHAR(20)  comment '城市',
    district VARCHAR(20)  comment '行政区',
    power_type VARCHAR(20)  comment '动力类型',
    market_level VARCHAR(20)  comment '市场级别',
    grade_level VARCHAR(20)  comment '档次等级',
    child_field_name VARCHAR(20)  comment '子字段名称,主要包括车身类型、市场级别、细分级别、档次等级、车型品牌、厂家名称、车型血缘',
    child_field_value VARCHAR(20)  comment '子字段值，需要和子字段',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( id ),
    INDEX  child_field ( data_time, city, child_field_name, child_field_value, market_level, grade_level, power_type)
);

/*
第五张表：
创建市场级别与车身类型关联统计表
*/
create table if not exists cartype_market_level_statistics(
    id INT NOT NULL AUTO_INCREMENT,
    data_time DATE comment '时间',
    province VARCHAR(20) comment '省份',
    city  VARCHAR(20)  comment '城市',
    district VARCHAR(20)  comment '行政区',
    power_type VARCHAR(20)  comment '动力类型',
    market_level VARCHAR(20)  comment '市场级别',
    car_type VARCHAR(20)  comment '车身类型',
    child_field_name VARCHAR(20)  comment '子字段名称,主要包括车身类型、市场级别、细分级别、档次等级、车型品牌、厂家名称、车型血缘',
    child_field_value VARCHAR(20)  comment '子字段值，需要和子字段',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( id ),
    INDEX  child_field ( data_time, city, child_field_name, child_field_value, market_level, car_type, power_type)
);


/*
第六张表：
创建档次等级与车身类型关联统计表
*/
create table if not exists cartype_grade_level_statistics(
    id INT NOT NULL AUTO_INCREMENT,
    data_time DATE comment '时间',
    province VARCHAR(20) comment '省份',
    city  VARCHAR(20)  comment '城市',
    district VARCHAR(20)  comment '行政区',
    power_type VARCHAR(20)  comment '动力类型',
    grade_level VARCHAR(20)  comment '市场级别',
    car_type VARCHAR(20)  comment '车身类型',
    child_field_name VARCHAR(20)  comment '子字段名称,主要包括车身类型、市场级别、细分级别、档次等级、车型品牌、厂家名称、车型血缘',
    child_field_value VARCHAR(20)  comment '子字段值，需要和子字段',
    watch_num int comment '关注人数',
    intent_num int comment '兴趣人数',
    like_num int comment '意向人数',
    buy_num int comment '到店人数',
    PRIMARY KEY ( id ),
    INDEX  child_field ( data_time, city, child_field_name, child_field_value, grade_level, car_type, power_type)
);
