1. Semantic Tag

    header, section, footer

   

2. input Tag

   ```html
   <body>
     <form action="#login">
       <div>
         <label for="username" style="font-weight: bold;" >USERNAME : </label>
         <input type="text" id="username" name="username" placeholder="아이디를 입력 해 주세요." autofocus>
       </div>
       <div>
         <label for="PWD" style="font-weight: bold;">PWD : </label>
         <input type="password" id="PWD" name="PWD" autofocus>
         <input type="submit" value="로그인">
       </div>
     </form>
   </body>
   ```

3. 크기 단위

   rem

   

4. 선택자

   자손 결합자는 p가 div에 포함되어 있기만 하면 적용이 된다.

   그러나 자식 결합자는 p가 div 바로 다음 단계에 포함되지 않는다면 적용되지 않는다.

   따라서 `<div><span><p>안녕하세요</p></span></div> `는 자손 결합자를 사용할 경우 크림슨으로 출력되지만, 자식 결합자를 사용할 경우 적용되지 않는다.
