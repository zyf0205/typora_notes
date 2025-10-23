# 创建部件

以当前活动屏幕为父对象创建基础部件(画布)

```
lv_obj_t *obj1=lv_obj_create(lv_scr_act());
```

# 大小

```
lv_obj_set_width(obj1,200);
lv_obj_set_hight(obj1,200);
lv_obj_set_size(obj1,200,400);
```

# 位置

设置部件位置时，坐标原点在父对象的左上角

同时设置x,y轴坐标（部件的左上角）

```
lv_obj_set_pos(obj1,200,200);
```

# 对齐

1.参照父对象对齐，不进行偏移

```
lv_obj_set_align(obj1,LV_ALIGN_...);
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741959628371-4aee98b1-a102-4c37-b23a-b9dae23979ed.png)

参照父对象对齐，再进行偏移

```
lv_obj_align(obj,LV_ALIGN_...,X,Y);
```

2.参照其他对象对齐，无父子关系

obj2相对于obj1对齐

```
lv_obj_align_to(obj2,obj1,LV_ALIGN_...,X,Y);
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741959939972-e3eb1667-3f0f-410b-8f7a-1338a9e01d3b.png)

# 样式（设置外观，优化交互）

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741960861112-ed0990f9-5611-43a9-9e85-d0e38aa67e26.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741961595817-032a210a-20b9-4b6a-8d25-f4bb2bffafb7.png)

## 背景

1.添加普通样式(可以共享)：

定义样式变量(必须是静态全局变量或动态分配)

```
static lv_style_t style;
```

初始化变量（开辟空间，给值清零）

```
lv_style_init(&style);
```

设置背景颜色

```
lv_style_set_bg_color(&style,lv_color_hex(0xf4b183));
```

创建部件

```
lv_obj_t *obj1=lv_obj_create(lv_scr_act());
```

添加样式

```
lv_obj_add_style(obj1,&style,LV_STATE_DEFAULT);
```

2.添加本地样式（不可以共享）

创建部件

```
lv_obj_t *obj1=lv_obj_create(lv_scr_act());
```

设置部件样式

```
lv_obj_set_style_bg_color(obj1,lv_color_hex(0xf4b183),LV_STATE_DEFAULT);
```

## 边框

设置边框样式

```
lv_obj_set_style_border_color (obj1,lv_color_hex(0x56c94c),LV_STATE_DEFAULT);
```

设置边框宽度

```
lv_obj_set_style_border_width(obj1,10,LV_STATE_DEFAULT);
```

设置边框透明度(0-255)越大越不透明

```
lv_obj_set_style_border_opa(obj1,200,LV_STATE_DEFAULT);
```

## 轮廓（边框外面的一圈）

设置轮廓样式

```
lv_obj_set_style_outline_color (obj1,lv_color_hex(0x56c94c),LV_STATE_DEFAULT);
```

设置轮廓宽度

```
lv_obj_set_style_outline_width(obj1,10,LV_STATE_DEFAULT);
```

设置轮廓透明度(0-255)越大越不透明

```
lv_obj_set_style_outline_opa(obj1,200,LV_STATE_DEFAULT);
```

# 事件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741962131559-7d310ad4-b714-4c09-af32-bc8a2adc5488.png)

事件代码网址：

```
https://lvgl.100ask.net/master/details/base-widget/event.html#event-codes
```

添加事件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741962479439-a84f41e1-c634-4857-bd6a-012dd20d1c65.png)

在回调函数中判断触发回调的事件代码

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741962564329-165945a2-831a-400e-b2a9-a4bb2b8e21d0.png)

在回调函数中判断触发回调的部件是哪个

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741962692771-1361031d-6d5c-4df5-804a-4bd89a90ad22.png)

# 标签部件（用于文本显示）

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741962962397-b87737fc-714b-4128-b86a-e76af34f2731.png)

文本设置

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741963277416-c07e7b42-5967-4c29-8412-23ab5477e84a.png)

设置的背景颜色默认透明度为0，要执行以下代码提升透明度才能看见

```
lv_obj_set_style_bg_opa(obj1,200,LV_STATE_DEFAULT);
```

要使用字体需要把对应的宏打开

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741963326849-e2a46408-dd38-4cad-a442-56bb7254c983.png)

设置文本透明度（可用于文字阴影）

```
lv_obj_set_style_text_opa(obj1,200,LV_STATE_DEFAULT);
```

长文本模式

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1741963531557-fd826001-a8b9-485b-93c8-8f0645caa523.png)

# 按钮部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742047878993-1152eea5-6f43-41b0-be6c-acf46e8b5494.png)

开启状态切换

```
lv_obj_add_flag(btn,LV_OBJ_FLAG_CHECKABLE);
```

添加事件(要添加事件必须开启状态切换)

```
lv_obj_add_event_cb(btn,event_cb,LV_EVENT_VALUE_CHANGED,NULL);
```

# 开关部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742048702661-8cae5d3c-b2b2-485a-a955-2aafca3d937f.png)

创建开关

```
lv_obj_t *switch1=lv_switch_create(lv_scr_act());
```

开关开启时,主体看不见

开关关闭时,指示器看不见

设置主体背景颜色

```
lv_obj_set_style_bg_color(switch1,lv_color_hex(0x1A2B40),LV_PART_MAIN);
```



![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742049001491-29ba18df-8de7-494e-97b4-ed156ac9d501.png)

```
去掉LV_STATE_DISABLED就可以修改了
```

# 复选框部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742049548175-0a0a9f1a-9f20-4584-b869-8bf231507a2e.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742049562424-4bb2a44c-58b9-43f4-8c31-f27930e88746.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742049628731-d4fd4e6b-0990-4aaf-a6f4-8fee6553abed.png)

```
去掉LV_STATE_DISABLED就可以修改了
```

# 进度条部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742049758437-2e6ec8e8-d3c2-4327-adbe-010d80d4d067.png)

`范围值`设置和`动画`设置都在设置`当前值`之前

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742049772694-eba35f49-1ef6-4bc5-8803-ddcd56a8db81.png)

开启动画  :  `LV_ANIM_ON `

# 加载器部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742050201135-5bbdfbf1-7ffe-47d1-9e7b-47daff885107.png)

# led部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742050435975-83079aeb-cf61-4244-906a-4141d20ed982.png)

快速居中对齐部件

```
lv_obj_center(led);
```

# 列表部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742050712014-f30bb7b6-69eb-47c1-b58c-5ba7568c8514.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742050732365-d6c7626a-df33-4b95-9e8f-0d1757433d75.png)

lvgl特殊字体枚举:

```
https://lvgl.100ask.net/master/details/main-components/font.html#special-fonts
```

# 下拉列表部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051232513-84ddde13-529e-4c4e-851a-a36f280bb752.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051249586-c8ef2165-b5ef-42b0-980a-edf4c70d6232.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051346309-2cf57429-44ba-4450-b003-e7abbb0dd59a.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051439579-8cd84b4c-1aac-4bda-84b5-dbfe1e44b6ff.png)

# 滚轮部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051515883-daa47a82-297e-4c18-8bd8-8c2ca34f0ebc.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051543388-3b1f9c21-44f1-4b5f-b1d5-83e2016765dc.png)

```
索引从0开始
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051652115-eafd1b5e-2dc4-482d-a064-fbbb9ba70403.png)

# 滑块部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051745973-a5a6da3a-c911-4245-a650-bb5704fb54e7.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051764098-0ff98099-2b86-4131-b992-1635052e0f73.png)

```
三种模式
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051850732-02bd3b07-9652-4730-9d1e-ece1df509b2b.png)

# 圆弧部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742051995015-f6062fbd-0e9d-4e9e-ad40-5911036b104c.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052002770-61b8ff12-1e92-472a-a26c-8d8dad2e6158.png)

```
背景弧`设置在`前景弧`设置`之前
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052162992-f2b5582c-d09f-4b2d-b849-8c9388e3d0bf.png)![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052212147-d40bf8d7-2a77-4416-ae43-dc38e1ce2a9a.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052235561-494adf1a-0d20-4d02-a556-e7416b4476ab.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052328765-ee735561-908f-4f4e-be75-b20e67ec7404.png)

# 线条部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052391999-fab0e0fc-a13b-4071-8160-f75137549831.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052410734-da040bd5-8c2a-41ae-8e77-fb5ba83c3c24.png)

```
Y轴反转效果
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052544395-9cfd7456-5992-452f-98e2-7272dc2ced28.png)

# 图片部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052702661-468465af-6eee-4f4c-9513-e2cdb935d323.png)

lvgl官方图片转数组

```
https://lvgl.io/tools/imageconverter
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742052999582-e5273b3d-2536-4ce2-abeb-c6550053999f.png)

# 色环部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742053171765-5c3ac189-09f9-42b3-8427-2b509fe80e09.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742053179103-b56823b2-cf51-454d-999d-c08c07eeb8b2.png)

```
长按会导致色环模式切换,可以固定色环模式
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742053238717-0fcdb589-9cdb-4190-961a-d7034973e86b.png)

设置色环圆弧宽度

```
lv_obj_set_style_arc_width(cw,20,LV_PART_MAIN);
```

# 按钮矩阵部件(更轻量化)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742053507301-9f0be0a2-ed3d-4643-8b38-4725d1bfbc0f.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742053528179-970d4c1f-6e85-4da4-896f-a3b9dc749c1f.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742053715153-f78a703b-861b-428b-8981-b2bd43262a88.png)

```
矩阵按钮美化示例
```

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742054088670-b68046a0-db26-4ddc-bfae-6aff60cd9a1f.png)

# 文本区域部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742054141332-6a087da4-da8a-4b0c-8b9e-108c27e984b3.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742054188032-2e410eeb-80f7-4514-ab10-355c8d258c03.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742054275603-c1b13245-b209-49a1-95c0-3f7fba017705.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742054433063-92dc48d4-13a3-487c-adab-a5403bc82f96.png)

# 键盘部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742054522121-6564785a-a350-4683-a2b3-2446e0be50e4.png)

# 图片按钮部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742113404873-635af13d-004d-4dd2-a7bd-bed22f65c8d5.png)

# 选项卡部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742113886625-07342a33-b4d9-40a3-bcca-2ea7e4c529b7.png)

# 平铺视图部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742114060584-26c1a2e5-26c8-4542-a27a-31088fb70ae6.png)

参数:`先列后行`

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742114079607-6ea448f2-8549-40e5-a622-8a81bfaf429e.png)

移除滚动条

```
lv_obj_remove_style(tileview,NULL,LV_PART_SCROLLBAR);
```

# 窗口部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742114562294-bb9b1213-8814-4dfb-99fb-b2524698a548.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742114584210-560e6e7e-d89f-4c12-8281-66a83e34790b.png)

 设置圆角

```
lv_obj_set_style_radius(win,10,LV_STATE_DEFAULT);
```

美化图标示例:

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115022001-f6307b12-5af4-46e1-95bf-831f6f1fe520.png)

对应回调函数

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115144082-e7247b27-fa4c-47d6-b391-7fe989ed62ed.png)

# 消息框部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115207437-ae0c9e1a-a10f-4e99-b53c-6bea1c6a17b9.png)

消息框获取当前触发源必须带current

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115229984-c4535c77-c7d7-402e-a531-e402d2e4d281.png)

# 微调器部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115605061-b791ad05-94d8-4d33-b6f7-8d3ba77db325.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115613429-a510cb5f-fc49-4789-b9f4-8b556ded83c6.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115779168-0ceb9fb7-3da3-4c5a-915a-c69f94166dfd.png)

# 表格部件

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742115902568-9f93e352-cd2f-4821-8034-ffcb3fe9c320.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742116088206-34898def-a726-4759-a666-d3e084545cd9.png)

# 实体按键控制

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742116139351-a71b1653-45b4-412a-9b4e-397646eea8af.png)