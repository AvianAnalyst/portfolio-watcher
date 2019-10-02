<template>
    <div class="AddCompany">
        <input v-model="company_name" type="text">
        <button @click="sendUpName" type="button">Save!</button>
    </div>
</template>

<script>
    export default {
        name: "report",
        data(){
            return {
                company_name: null,
            };
        },
        methods: {
            sendUpName() {
                this.$emit('click', this.company_name);
                // eslint-disable-next-line no-console
                console.log(this.company_name);
            }
        },
    };
</script>
