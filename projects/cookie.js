const cookie = require('cookie');
const crypto = require('crypto')
const cookieName = 'weaver-device-id';
const cookieLifetime = 730;

const setCookie = true

const hex = [...Array(256).keys()].map((index) => index.toString(16).padStart(2, '0'));


var self_uuid = () => {
  const r = crypto.getRandomValues(new Uint8Array(16));

  r[6] = (r[6] & 0x0f) | 0x40;
  r[8] = (r[8] & 0x3f) | 0x80;

  return [...r.entries()].map(([index, int]) => ([4, 6, 8, 10].includes(index) ? `-${hex[int]}` : hex[int])).join('');
};

uuid = self_uuid()

response = {
    headers: {
        asdf: 'qwer'
    }
}

resHead = response.headers

resHead['set-cookie'] = {qwer: 'asdf'}

console.log(response)
// if (setCookie === true) {
//     // let domainTld = (requestHeaders.host[0].value).split(/\./).slice(-2).join('.');

//     // Build user cookie string with user UUID.
//     let cookieStringUser = cookie.serialize(cookieName, String(uuid), {
//         domain: '.wantedlab.com',
//         path: '/',
//         secure: true,
//         httpOnly: true,
//         sameSite: 'None',
//         maxAge: 60 * 60 * 24 * cookieLifetime 
//     });

//     // Set HTTP cookies in response.
//     responseHeaders['set-cookie'] = [{
//         key: ' set-cookie',
//         value: cookieStringUser
//     }];
//     console.log(cookieStringUser)
// }
