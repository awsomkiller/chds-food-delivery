import axios from 'axios';

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i += 1) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const axiosInstance = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
    'X-CSRFToken': getCookie('csrftoken'),
    // 'Authorization':'Token 877508fc5158f0e598822636476bb9fbccd42d13' //Not for prod, only for testing purpose
  },
});

export default axiosInstance;

// b331c415d9acc0840071ef5bbda6281212133f8d testuser

// 034499b43fabee3849b1309626e7db61477e4da1 user@gmail.com

// 5d744fd2bb18e4068a670bb891b2f3b600b7bf5b user@anil-workshop

// 877508fc5158f0e598822636476bb9fbccd42d13 user1@anil-workshop
