
          function insert(num) {
             document.form.textview.value = document.form.textview.value + num;
          }
          function clean() {
             document.form.textview.value = "";
          }
          function back() {
             var exp = document.form.textview.value;
             document.form.textview.value = exp.substring(0,exp.length-1);
          }
          function equal() {
             var eqv = document.form.textview.value;
             if(eqv) {
                document.history.textarea.value = document.history.textarea.value + document.form.textview.value+'='+eval(eqv)+"\n";
                document.form.textview.value = eval(eqv);
             }
          }
