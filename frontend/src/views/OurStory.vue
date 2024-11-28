<template>
    <section class="about-banner position-relative d-flex align-items-center justify-content-center">
      <div class="container-xl">
        <div class="heading text-center">
          <h1 class="text-white m-0">OUR STORY</h1>
        </div>
      </div>
    </section>
    <section class="our-story">
      <div class="container-xl">
        <div class="story-content text-center">
          <p>With over 25 years of experience in the fitness industry, we are passionate about creating not just aesthetically pleasing bodies, but sustainable, long-term healthy eating habits. Driven by a love for exploring different flavors, we have dedicated years to developing healthy, delicious recipes that you can enjoy for a lifetime.</p>
          <p class="pt-4">Our mission is simple: to make healthy eating both enjoyable and sustainable. We believe that a balanced, nourishing diet is the foundation of a happy life. With our meals, we aim to bring you joy and vitality, helping you live simply and eat well, while sustaining long-term health and happiness.</p>
        </div>
      </div>
    </section>
    <section class="choose position-relative">
      <div class="container-xl">
         <div class="heading text-center">
          <h1 class="text-white m-5 border-bottom pb-3 w-auto">Why People Choose Us</h1>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <div class="d-flex align-items-center justify-content-center mt-4">
              <div class="box-content first bg-white p-4">
                <p>Health-First Fusion</p>
                <p class="pt-2">We blend the best of traditional Chinese cuisine with modern, health-conscious ingredients, ensuring each meal is packed with balanced nutrition and rich, authentic flavors.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="row last">
          <div class="col-md-4">
           <div class="box-content bg-white p-4">
              <p>Freshly Made, Always</p>
              <p class="pt-2">Every meal is prepared fresh, from scratch, using high-quality, wholesome ingredients. No preservatives, no shortcuts—just clean, delicious food crafted to fuel your workout and recovery.</p>
            </div>
             <div class="box-content bg-white p-4 mt-4">
              <p>Exclusive Member Deals</p>
              <p class="pt-2">As a valued member, you get access to exclusive discounts and special meal deals designed just for you, offering both savings and variety to keep your diet exciting and sustainable.</p>
            </div>
          </div>
          <div class="col-md-4 d-flex justify-content-center align-items-center">
            <div class="image-content">
              <img src="../assets/meal.png" class="img-fluid">
            </div>
          </div>
           <div class="col-md-4">
           <div class="box-content bg-white p-4">
              <p>Deliciously Healthy</p>
              <p class="pt-2">We believe healthy food should be delicious. Our menu is carefully crafted to bring you the best in Chinese fusion flavors, offering meals that taste amazing while meeting all your nutritional needs.</p>
            </div>
             <div class="box-content bg-white p-4 mt-4">
              <p>Personalized Nutrition Guidance</p>
              <p class="pt-2">Our service includes access to one-on-one nutritional guidance to help you make informed choices that align with your fitness goals, ensuring every meal is both satisfying and supportive of your progress.</p>
            </div>
          </div>

        </div>
        <div class="row exclusive">
          <div class="col-sm-12">
            <div class="d-flex align-items-center justify-content-center mt-4">
              <div class="box-content first bg-white p-4">
                <p>Exclusive Gym Partnerships & Training Deals</p>
                <p class="pt-2">Enjoy special offers on training programs through our gym partnerships, combining the best in tailored meal plans with professional training for a fully integrated approach to wellness.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
	<FooterComponent />
</template>
<script setup>
import FooterComponent from '@/components/FooterComponent.vue';
</script>

<style>
section{
	padding: 40px 0;
}
section.about-banner{
	height: 250px;
}
section.about-banner::before{
	position: absolute;
	content: "";
	background: url('../assets/about-banner.png');
	background-size: cover;
	background-position: center;
	height: 100%;
	width: 100%;
	z-index: -1;
}
section .heading span{
	color: #944C22;
}
section.our-story .story-content p{
	color: #4e4e4e;
}
section.our-story .story-content{
	padding: 40px 0;
	font-family: "Poppins", sans-serif!important;
}
section.choose::before{
	position: absolute;
	top: 0;
	content: "";
	background: url('../assets/choose-bg.png');
	height: 100%;
	width: 100%;
	background-size: cover;
	background-attachment: fixed;
	z-index: -1;
	background-position: center;
}
section.choose p:first-child{
	font-size: 24px;
}
section.choose p:last-child{
	font-family: "Poppins", sans-serif!important;
	font-size: 16px;
	color: #4e4e4e;
}
section.choose .box-content{
	border-radius: 15px;
	transition: 0.5s ease all;
}
section.choose .row .box-content:hover{
	background: #944C22!important;
	cursor: pointer;
	color: #fff;
}
section.choose .row .box-content:hover p{
	color: #fff;
}
section.choose .row .box-content.first{
	width: 33.3%;
}
section.contact .social-icons{
	gap: 20px;
}
section.contact .social-icons i{
	box-shadow: rgb(100 100 111 / 50%) 0px 0px 10px 0px;
    transition: 0.5s ease all;
}
section.contact .social-icons i::before{
	padding: 10px;
	border-radius: 50%;
	width: 35px;
	height: 35px;
	display: flex;
    align-items: center;
    justify-content: center;
}
section.contact .social-icons i:hover::before{
	background: #944c22;
	cursor: pointer;
	background-position: left bottom !important;
}
section.contact .social-icons .icon:hover i{
	color: #fff;
	background: #944c22;
	cursor: pointer;
}



@media screen and (max-width: 991.91px){
	section.choose .row .box-content.first {
        width: 50%;
	}
	section.choose .col-md-4 {
        width: 33.3% !important;
	}
	section.choose .container{
		max-width: 90%;
	}
	section.choose .row.last{
		margin: 30px 0 0;
	}
	section.choose p:first-child {
        font-size: 18px;
	}
	section.choose p:last-child{
		font-size: 14px;
	}
	section.choose .box-content{
		padding: 15px!important;
	}
}

@media (max-width: 767.91px){
	section.choose .row .box-content.first {
        width: 100%;
	}
	section.choose .col-md-4{
		justify-content: center;
		margin: 20px 0;
		padding: 0;
	}
	section.choose .row.last {
        margin: 10px 0 0;
	}
	section.choose .row.exclusive .d-flex{
		margin: 10px 0 0!important;
	}
}

@media (max-width: 575px){
	.container{
		padding: 0 15px!important;
	}
	section.contact .reach-us{
		flex-wrap: wrap;
	}
	section.contact .social-icons{
		margin: 20px 0 0!important;
	}
}
</style>