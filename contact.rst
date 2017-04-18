Contact
-------

You can contact me using the below form.

.. raw:: html

  <form id="contactform" method="POST">
  <p align="center">
  <input type="email" name="_replyto" placeholder="Email" size=34>
  <input type="hidden" name="_subject" value="Website contact parmes.org" />
  <input type="text" name="_gotcha" style="display:none" />
  <input type="hidden" name="_next" value="./thankyou.html" />
  </p>
  <p align="center">
  <textarea name="text" placeholder="Your message" cols=36 rows=16></textarea>
  </p>
  <p align="center">
  <input type="submit" value="Send">
  </p>
  </form>
  <script>
     var contactform = document.getElementById('contactform');
     contactform.setAttribute('action', '//formspree.io/' + 'contact' + '.' + 'forms' + '.' + 'tk' + '@' + 'gmail' + '.' + 'com');
  </script>
