package com.net.qqcos2

import android.app.Activity
import android.graphics.Bitmap
import com.tencent.cos.xml.CosXmlService
import com.tencent.cos.xml.CosXmlServiceConfig
import com.tencent.cos.xml.exception.CosXmlClientException
import com.tencent.cos.xml.exception.CosXmlServiceException
import com.tencent.cos.xml.listener.CosXmlResultListener
import com.tencent.cos.xml.model.CosXmlRequest
import com.tencent.cos.xml.model.CosXmlResult
import com.tencent.cos.xml.transfer.COSXMLUploadTask
import com.tencent.cos.xml.transfer.COSXMLUploadTask.COSXMLUploadTaskResult
import com.tencent.cos.xml.transfer.TransferConfig
import com.tencent.cos.xml.transfer.TransferManager
import com.tencent.qcloud.core.auth.QCloudCredentialProvider
import com.tencent.qcloud.core.auth.ShortTimeCredentialProvider
import kotlin.reflect.KFunction4

object qqcos {
    private fun sq(context:Activity):CosXmlService{
        val region = "ap-chengdu"
        // 创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
        // 创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
        val serviceConfig = CosXmlServiceConfig.Builder()
            .setAppidAndRegion("1258802717",region)
            .setRegion(region)
            .setDebuggable(true)
            .isHttps(true) // 使用 HTTPS 请求, 默认为 HTTP 请求
            .builder()
        val secretId = "AKIDxgBQRH5uLbU9YiuKiru1fAXu63k4j4g3 " //永久密钥 secretId
        val secretKey = "IL9h5HG0Wv50iHdleMq54oNjslqcASUI" //永久密钥 secretKey
        val credentialProvider: QCloudCredentialProvider = ShortTimeCredentialProvider(secretId, secretKey, 300)
        val cosXmlService = CosXmlService(context, serviceConfig, credentialProvider)
        return cosXmlService
    }
    fun upload(context:Activity, srcPath:String):COSXMLUploadTask{
        // 初始化 TransferConfig
        var transferConfig = TransferConfig.Builder().build()
        val transferManager = TransferManager(sq(context), transferConfig)
        val bucket = "qjt-1258802717" //存储桶，格式：BucketName-APPID
        val cosPath = "" //对象在存储桶中的位置标识符，即称对象键
        val uploadId: String? = null //若存在初始化分块上传的 UploadId，则赋值对应的 uploadId 值用于续传；否则，赋值 null
        val cosxmlUploadTask = transferManager.upload(bucket, srcPath, srcPath, uploadId)
        return cosxmlUploadTask
    }
}