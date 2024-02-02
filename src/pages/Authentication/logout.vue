<template>
  <div class="q-pa-md q-gutter-md q-vh-center">
<!-- <q-img
        src="url"
        spinner-color="white"
        style="margin:0 auto 10px auto;display: block;height: 44px; width:199px"
      ></q-img> -->

<div class="q-gutter-md justify-center q-ma-md self-center ">
<div class=" q-gutter-md q-ma-md text-center">
  <q-avatar size="110px" class="text bordered-2" bordered font-size="22px" color="teal" text-color="white" >DailyKhata
  </q-avatar>

<q-btn label="SignUp in DailyKhata" to="signup" style="width: 300px;" class=" text-capitalize" color="green"/>
<q-btn label="login" to="login" style="width: 300px;" class=" text-black bg-white text-capitalize" color="whites"/>

  <q-btn label="Sign In with Google"
  type="button"
  class="bg-white logo text-capitalize"
  style="width: 300px;"
  @click="signInWithGoogle"
 >
    <!-- <q-icon type="logo" name="google"/> -->
</q-btn>
</div>
</div>
</div>

</template>
<script>


export default {

  data(){
    return{

    }
  },

  methods:{
    login(){
      this.$router.push('login')
      // alert("asdbabs")
    },

    // signInWithGoogle() {
    //   // Use Google's API to trigger the sign-in process
    //   gapi.auth2.getAuthInstance().signIn().then(
    //     // Handle successful sign-in
    //     googleUser => {
    //       // Access user information from googleUser
    //       const profile = googleUser.getBasicProfile();
    //       console.log('ID: ' + profile.getId());
    //       console.log('Name: ' + profile.getName());
    //       console.log('Image URL: ' + profile.getImageUrl());
    //       console.log('Email: ' + profile.getEmail());

    //       // You can implement further actions here, such as sending user data to your server.
    //     },
    //     // Handle sign-in errors
    //     error => {
    //       console.error('Google Sign-In Error:', error);
    //     }
    //   );
    // },
  },
  mounted() {
    // Initialize the Google API on component mount
    // gapi.load('auth2', () => {
    //   gapi.auth2.init({
    //     client_id: 'YOUR_GOOGLE_CLIENT_ID', // Replace with your Google Client ID
    //   });
    // });
  }
}
</script>
<!--
<style>
.login-with-google-btn {
  transition: background-color .3s, box-shadow .3s;

  padding: 12px 16px 12px 42px;
  border: none;
  border-radius: 3px;
  box-shadow: 0 -1px 0 rgba(0, 0, 0, .04), 0 1px 1px rgba(0, 0, 0, .25);

  color: #757575;
  font-size: 14px;
  font-weight: 500;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Fira Sans","Droid Sans","Helvetica Neue",sans-serif;

  background-image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNMTcuNiA5LjJsLS4xLTEuOEg5djMuNGg0LjhDMTMuNiAxMiAxMyAxMyAxMiAxMy42djIuMmgzYTguOCA4LjggMCAwIDAgMi42LTYuNnoiIGZpbGw9IiM0Mjg1RjQiIGZpbGwtcnVsZT0ibm9uemVybyIvPjxwYXRoIGQ9Ik05IDE4YzIuNCAwIDQuNS0uOCA2LTIuMmwtMy0yLjJhNS40IDUuNCAwIDAgMS04LTIuOUgxVjEzYTkgOSAwIDAgMCA4IDV6IiBmaWxsPSIjMzRBODUzIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNNCAxMC43YTUuNCA1LjQgMCAwIDEgMC0zLjRWNUgxYTkgOSAwIDAgMCAwIDhsMy0yLjN6IiBmaWxsPSIjRkJCQzA1IiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNOSAzLjZjMS4zIDAgMi41LjQgMy40IDEuM0wxNSAyLjNBOSA5IDAgMCAwIDEgNWwzIDIuNGE1LjQgNS40IDAgMCAxIDUtMy43eiIgZmlsbD0iI0VBNDMzNSIgZmlsbC1ydWxlPSJub256ZXJvIi8+PHBhdGggZD0iTTAgMGgxOHYxOEgweiIvPjwvZz48L3N2Zz4=);
  background-color: white;
  background-repeat: no-repeat;
  background-position: 12px 11px;

  &:hover {
    box-shadow: 0 -1px 0 rgba(0, 0, 0, .04), 0 2px 4px rgba(0, 0, 0, .25);
  }

  &:active {
    background-color: #eeeeee;
  }

  &:focus {
    outline: none;
    box-shadow:
      0 -1px 0 rgba(0, 0, 0, .04),
      0 2px 4px rgba(0, 0, 0, .25),
      0 0 0 3px #c8dafc;
  }

  &:disabled {
    filter: grayscale(100%);
    background-color: #ebebeb;
    box-shadow: 0 -1px 0 rgba(0, 0, 0, .04), 0 1px 1px rgba(0, 0, 0, .25);
    cursor: not-allowed;
  }
}

body {
  text-align: center;
  padding-top: 2rem;
}
</style> -->
