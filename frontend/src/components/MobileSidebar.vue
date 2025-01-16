<script>
import NavbarMenu from './NavbarMenu.vue';


NavbarMenu
    export default {
        components: {
            NavbarMenu,
        }
    }
</script>
<template>

 

    <div class="offcanvas offcanvas-start" tabindex="-1" id="mobilemenu" aria-labelledby="mobilemenuLabel">
        <div class="offcanvas-header">
            <h6 class="offcanvas-title" id="mobilemenuLabel">Chi Hun Da Su</h6>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <NavbarMenu />
        </div>
    </div>
</template>