/*
创建一个数据库saas
*/
# create database saas;

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
