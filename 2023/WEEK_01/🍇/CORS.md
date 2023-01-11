### CORS error

<hr>

#### CORS error ?

**CORS**란, Cross Origin Resource Sharing의 약자로 **서로 다른 Origin간의 리소스 교환**을 뜻한다.

**Origin**은 url 주소상에서 **프로토콜, Domain 이름, 포트**까지 포함한 개념이다. **CORS 에러는 서로 다른 Origin에서 리소스를 교환할 때 브라우저에서 내뿜는 에러를 말한다.**

간단히 말해 **내 서버와 다른 서버의 리소스를 가져오면서** 발생되는 브라우저 에러이다.

![Origin](C:\Study\2023\WEEK_01\🍇\Origin.PNG)

```javascript
<script>
    // 간단하게 현재 사이트의 Origin 찾기 
	console.log(location.origin);
</script>
```

<hr>

* **SOP(Same Origin Policy : 동일 출처 정책)**

'동일한 출처에서만 리소스(이미지, 영상 등)을 공유할 수 있다'는 정책으로 다른 출처 서버의 리소스는 가져올 수 없다. 출처가 다른 서버의 리소스도 자유롭게 가져올 수 있게 되면 보안에 취약해지기 때문이다.

![Same Origin Policy](C:\Study\2023\WEEK_01\🍇\SOP CORS.png)



* **CORS(Cross Origin Resource Sharing : 교차 출처 자원 공유 )**

본래 SOP 정책으로 출처가 다르면 리소스를 가져올 수 없지만, CORS 정책을 따르면 SOP 정책을 위반해도 다른 출처의 리소스를 가져오는 것을 허용한다. [CORS 정책](https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-CORS-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%F0%9F%91%8F)



같은 Origin에서는 요청/처리하는 곳이 동일하기 때문에 보안상 처리할 필요가 없다. 하지만 **다른 Origin에서 오는 요청**이라면 요청의 결과값이 믿을만한지 **검증이 필요**하다.

브라우저에서는 localhost:8080 서버에서 전달 받은 응답중 헤더에 Access-Control-Allow-Origin 값을 확인하고 이 값에 현재 Origin이 포함되는지 확인해서, 포함되어 있으면 CORS를 수행하고, 아니면 에러를 낸다.

curl 이나 postman을 이용해 서버에 요청하면 문제 없이 응답이 오는데, 프론트 작업을 할 때만 CORS 에러가 발생하는 것도 브라우저가 미리 보고 개입하기 때문이다. 

![CORS Error easy](C:\Study\2023\WEEK_01\🍇\CORS Error easy.png)

<hr>

#### CORS 해결방법  [참고 코드](https://selfish-developer.com/entry/%EC%A7%80%EA%B8%8B%EC%A7%80%EA%B8%8B%ED%95%9C-CORS-error-%EC%9D%B4%EC%A0%9C-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EA%B3%B5%EB%B6%80%ED%95%B4%EB%B3%B4%EC%9E%90)

**1. Access-Control-Allow-Origin 전체 허용**

백엔드에서 모든 주소를 Access-Control-Allow-Origin 으로 주면 간단히 해결된다. 단, 이럴 경우 검증되지 않은 모든 주소를 허용해주는 것이기 때문에 보안이 취약해질 수 있다는 단점이 있다.



**2. 프록시 서버 사용**

브라우저에서 보낸 요청을 프론트에서 받아서 대신 보내는 방법이다. CORS는 브라우저 에러로 서버간의 데이터 교환상에서는 CORS가 이뤄지지 않기 때문에 프론트 서버에서 받은 데이터를 브라우저에 업데이트 하면 된다. 