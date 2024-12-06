<template>
    <section class="about-banner position-relative d-flex align-items-center justify-content-center">
      <div class="container-xl">
        <div class="heading text-center">
          <h1 class="text-white m-0">{{ t('our-story-heading', ['our-story']) }}</h1>
        </div>
      </div>
    </section>
    <section class="our-story">
      <div class="container-xl">
        <div class="story-content text-center">
          <p>{{ t('our-story-description-1', ['our-story']) }}</p>
          <p class="pt-3">{{ t('our-story-description-2', ['our-story']) }}</p>
        </div>
      </div>
    </section>
    <section class="choose position-relative">
      <div class="container">
         <div class="heading text-center">
          <h1 class="text-white m-lg-5 m-md-3 border-bottom pb-3 w-auto">{{ t('choose-us-heading', ['our-story']) }}</h1>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <div class="d-flex align-items-center justify-content-center mt-4">
              <div class="box-content first bg-white p-4">
                <p class="fw-bold" >{{ t('health-first-fusion-heading', ['our-story']) }}</p>
                <p class="pt-2">{{ t('health-first-fusion-heading-description', ['our-story']) }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="row last">
          <div class="col-md-4">
           <div class="box-content bg-white p-4">
              <p class="fw-bold">{{ t('member-deals-heading', ['our-story']) }}</p>
              <p class="pt-2">{{ t('member-deals-description', ['our-story']) }}</p>
            </div>
             <div class="box-content bg-white p-4 mt-4">
              <p class="fw-bold">{{ t('freshly-made-heading', ['our-story']) }}</p>
              <p class="pt-2">{{ t('freshly-made-description', ['our-story']) }}</p>
            </div>
          </div>
          <div class="col-md-4 d-flex justify-content-center align-items-center">
            <div class="image-content">
              <img src="../assets/meal.png" class="img-fluid">
            </div>
          </div>
           <div class="col-md-4">
           <div class="box-content bg-white p-4">
              <p class="fw-bold">{{ t('deliciously-healthy-heading', ['our-story']) }}</p>
              <p class="pt-2">{{ t('deliciously-healthy-description', ['our-story']) }}</p>
            </div>
             <div class="box-content bg-white p-4 mt-4">
              <p class="fw-bold">{{ t('personalized-nutrition-guidance-heading', ['our-story']) }}</p>
              <p class="pt-2">{{ t('personalized-nutrition-guidance-description', ['our-story']) }}</p>
            </div>
          </div>

        </div>
        <div class="row exclusive">
          <div class="col-sm-12">
            <div class="d-flex align-items-center justify-content-center mt-4">
              <div class="box-content first bg-white p-4">
                <p class="fw-bold">{{ t('exclusive-gym-partnerships-heading', ['our-story']) }}</p>
                <p class="pt-2">{{ t('exclusive-gym-partnerships-description', ['our-story']) }}</p>
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
import { useTranslationStore } from '@/stores/translation';

const translationStore = useTranslationStore();

const t = (label, modules) => {
	return translationStore.translate(label, modules);
};

</script>

<style>
section.choose {
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
	/* section.choose .col-md-4 {
        width: 33.3% !important;
	} */
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
	/* .container{
		padding: 0 15px!important;
	} */
	section.contact .reach-us{
		flex-wrap: wrap;
	}
	section.contact .social-icons{
		margin: 20px 0 0!important;
	}
}
</style>