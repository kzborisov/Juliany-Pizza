function passwordResetSuccess(redirectUrl) {
    window.onload = function () {
        alert("Password reset was successful! You can login with your new password now.");
        window.location.href = redirectUrl;
    }
}


function passwordResetEmailSent(redirectUrl) {
    window.onload = function () {
        alert("We've e-mailed you instructions for setting your password to the e-mail address you submitted. You should be receiving it shortly.");
        window.location.href = redirectUrl;
    }
}