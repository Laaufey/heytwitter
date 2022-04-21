
function returnFalse(){
  if (document.myForm.myText.value == '')
      return false;
      // When it returns false - your form will not submit and will not redirect too
  else
      return true;
   // When it returns true - your form will submit and will redirect
// (actually it's a part of submit) id you have mentioned in action
};

function showTweetModal(){
  // alert();
  const modal = document.getElementById("tweetModal").classList.remove("hidden");

};

function hideTweetModal(){
  // alert();
  const modal = document.getElementById("tweetModal").classList.add("hidden");

};

function toggleTweetModal(){
  // alert();
  const modal = document.getElementById("tweetModal").classList.toggle("hidden");

};

