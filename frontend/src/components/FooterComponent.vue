<script setup>
import { useTranslationStore } from '@/stores/translation';

const translationStore = useTranslationStore();

const t = (label, modules) => {
      return translationStore.translate(label, modules);
    };
</script>
<template>
<footer class="footer-section bg-title fix">
    <div class="footer-widgets-wrapper">
        <div class="shape1 float-bob-y d-none d-xxl-block">
            <img src="@/assets/homepage/footerShape1_1.png" alt="shape" />
        </div>

        <div class="shape3 d-none d-xxl-block">
            <img src="@/assets/homepage/footerShape1_3.png" alt="shape" />
        </div>
        <div class="shape4 d-none d-xxl-block">
            <img src="@/assets/homepage/footerShape1_4.png" alt="shape" />
        </div>
        <div class="container p-lg-3 p-md-">
            <div class="footer-top">
                <div class="row gy-4">
                    <div class="col-lg-4">
                        <div class="fancy-box">
                            <div class="item1">
                                <i class="fa-solid fa-location-dot"></i>
                            </div>
                            <div class="item2">
                                <h6>{{ t('address', ['footer']) }}</h6>
                                <p>{{ t('restaurant_address', ['footer']) }}</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 d-flex justify-content-start justify-content-lg-end">
                        <div class="fancy-box">
                            <div class="item1"><i class="fa-solid fa-envelope"></i></div>
                            <div class="item2">
                                <h6>{{ t('send_email', ['footer']) }}</h6>
                                <p>info@chds.com.au</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 d-flex justify-content-start justify-content-lg-end">
                        <div class="fancy-box">
                            <div class="item1">
                                <i class="fa-solid fa-phone"></i>
                            </div>
                            <div class="item2">
                                <h6>{{ t('customer_care', ['footer']) }}</h6>
                                <p>04 6846 2068 </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

          <div class="row">
                <div
                class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12 p-3"
                data-wow-delay=".2s"
                style="
                    visibility: visible;
                    animation-delay: 0.2s;
                    animation-name: fadeInUp;
                ">
                        <div class="single-footer-widget">
                            <div class="widget-head mb-2">
                                <a href="index.html">
                                    <img src="@/assets/homepage/CHDS logo White transparent.png" class="logo-white" alt="logo-img" />
                                </a>
                            </div>
                            <div class="footer-content">

                                <div class="social-icon d-flex align-items-center">
                                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                                    <a href="#"><i class="fab fa-twitter"></i></a>
                                    <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                                    <a href="#"><i class="fa-brands fa-youtube"></i></a>
                                </div>

                            </div>
                        </div>
                </div>

                <div
                class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12 p-3"
                data-wow-delay=".2s"
                style="
                    visibility: visible;
                    animation-delay: 0.2s;
                    animation-name: fadeInUp;
                ">
                        <div class="single-footer-widget">

                            <div class="footer-content">
                                <figure class="wpb_wrapper vc_figure">
                                    <div class="vc_single_image-wrapper   vc_box_border_grey">
                                        <img width="200" height="200" src="@/assets/CHDS-Wechat.webp">
                                    </div>
                                </figure>
                            </div>
                        </div>
                </div>


                <div
                class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12 p-3"
                data-wow-delay=".4s"
                style="
                    visibility: visible;
                    animation-delay: 0.4s;
                    animation-name: fadeInUp;
                ">
                        <div class="single-footer-widget">
                            <div class="widget-head">
                                <h3>{{ t('quick_links', ['footer']) }}</h3>
                            </div>
                            <ul class="list-area">
                                <li>
                                    <router-link to="/">
                                        <i class="fa-solid fa-angles-right"></i>
                                        {{ t('home', ['footer']) }}
                                    </router-link>
                                </li>
                                <li>
                                    <router-link to="/ordernow">
                                        <i class="fa-solid fa-angles-right"></i>
                                        {{ t('order_now', ['footer']) }}
                                    </router-link>
                                </li>
                                <li>
                                    <router-link to="/ourstory">
                                        <i class="fa-solid fa-angles-right"></i>
                                        {{ t('our_story', ['footer']) }}
                                    </router-link>
                                </li>
                                <li>
                                    <router-link to="/contact-us">
                                        <i class="fa-solid fa-angles-right"></i>
                                        {{ t('contact_us', ['footer']) }}
                                    </router-link>
                                </li>
                            </ul>
                        </div>
                </div>

                <div
                    class="col-xl-3 col-lg-4 col-md-6 col-sm-6 col-12 p-3"
                    data-wow-delay=".4s"
                    style="
                        visibility: visible;
                        animation-delay: 0.4s;
                        animation-name: fadeInUp;
                    ">
                        <div class="single-footer-widget">
                            <div class="widget-head">
                                <h3>{{ t('available_timing', ['footer']) }}</h3>
                            </div>
                            <ul class="list-area">
                                <li class="mb-2">
                                    {{ t('monday_wednesday_friday', ['footer']) }}
                                </li>
                                <li>
                                    <span class="text-theme-color2"> 2:30pm - 8pm </span>
                                </li>
                            </ul>
                            
                        </div>
                    </div>
                
                
              </div>
           
        </div>
    </div>
    <div class="footer-bottom">
        <div class="container">
            <div class="footer-wrapper d-flex align-items-center justify-content-center">
                <p class="wow fadeInLeft mb-0" data-wow-delay=".3s" style="
                visibility: visible;
                animation-delay: 0.3s;
                animation-name: fadeInLeft;
              ">
                    {{ t('chi_hun_da_su_2024_all_rights_reserved', ['footer']) }}
                </p>
            </div>
        </div>
    </div>
</footer>
</template>

<style>

</style>
