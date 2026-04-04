`navigator.geolocation.getCurrentPosition` 是网页应用中常用的获取设备位置的 API，对该函数进行重载可以“欺骗”网页的定位系统．

`getCurrentPosition` 的语法如下：

```js
getCurrentPosition(success)
getCurrentPosition(success, error)
getCurrentPosition(success, error, options)
```

根据 [mdn](https://developer.mozilla.org/zh-CN/docs/Web/API/Geolocation/getCurrentPosition) 所述，参数的含义如下：

+ `success` 是函数成功时的回调函数，唯一输入参数是 `GeolocationPosition`，包含两个属性：
    + `coords` 的类型是 `Coordinates`，表示设备在地球上的位置，具体属性如下：
        + `latitude`：纬度（十进制，`double`）；
        + `longitude`：经度（十进制，`double`）；
        + `altitude`：海拔（`double`），可以为 `null`（表示无法提供，下同）；
        + `accuracy`：位置精度（单位米，`double`）；
        + `altitudeAccuracy`，海拔精度（单位米，`double`），可以为 `null`；
        + `heading`：设备行驶方向（单位为度，`double`），`0` 度表示正北，方向按顺时针确定，可以为 `null`；
        + `speed`：设备速度（单位米每秒，`double`），可以为 `null`．
   + `timestamp`，返回一个[时间戳](https://developer.mozilla.org/zh-CN/docs/Glossary/Unix_time)，表示获取到数据的时间．
+ `error` 是函数失败时的回调函数，唯一输入参数是 `GeolocationPositionError`，包含两个属性：
    + `code` 错误码：
        + `1` / `PERMISSION_DENIED`：权限获取失败；
        + `2` / `POSITION_UNAVAILABLE`：内部位置源返回内部错误；
        + `3` / `TIMEOUT`：获取地理位置超时；
    + `message` 开发者可读的错误信息．
+ `options` 是一个包含下列参数的可选对象：
    + `maximumAge`：一个正的 `long` 值，表示可接受的缓存位置的最大存在时间（以毫秒为单位）．如果设置为 `0`，则设备不能使用缓存位置，必须尝试检索当前的真实位置；如果设置为 `Infinity`，则设备必须返回缓存位置而不考虑其存在时间．默认值：`0`．
    + `timeout`：一个正的 `long` 值，表示设备允许获取位置的最长时间（以毫秒为单位）．默认值为 `Infinity`，意味着 `getCurrentPosition()` 会一直等待直到位置可用才返回．
    + `enableHighAccuracy`：一个布尔值，指示应用程序希望接收尽可能精确的位置结果．如果为 `true`，且设备能够提供更高精度的位置，则会启用高精度模式；这可能导致响应时间变慢或功耗增加．如果为 `false`，设备可通过更快响应和/或更少功耗来节省资源．默认值：`false`．


因此，一个简单的欺骗脚本为：

```js
const originalGetCurrentPosition = navigator.geolocation.getCurrentPosition;

navigator.geolocation.getCurrentPosition = function(success, error, options) {
    const fakePosition = {
        coords: {
            latitude: 0.0,
            longitude: 0.0,
            accuracy: 10,
            altitude: null,
            altitudeAccuracy: null,
            heading: null,
            speed: null
        },
        timestamp: Date.now()
    };
    success(fakePosition);
};
```

只需在开发者工具中的控制台执行即可．
